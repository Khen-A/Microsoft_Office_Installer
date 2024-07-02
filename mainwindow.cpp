#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "qevent.h"
#include "checkinstaller.h"
#include <QScreen>
#include <QFile>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonArray>
#include <QDir>
#include <Windows.h>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    Path = QCoreApplication::applicationDirPath();
    Initialize_Data();
    Initialize_File();

    isWindowMove = false;
    isDownloading = false;
    isCancelDownload = false;
    isFailedToDownload = false;
    isInstalling = false;
    isFailedToInstall = false;

    oldPos = QPoint(0, 0);
    QString ProductID = JsonData.value("ProductID").toString();
    QString BuildNo = JsonData.value("BuildNo").toString();
    int total_byte = JsonData.value("Total_Byte").toInt();

    ui->HeaderGrid->installEventFilter(this);
    ui->CloseButton->installEventFilter(this);

    ui->ProductIDLabel->setText(ProductID);
    ui->VersionLabel->setText("v" + BuildNo);
    ui->ArchitectureLabel->setText("x" + Converted_Architecture());

    ui->progressBar->setValue(0);
    ui->progressBar->setMaximum(total_byte);
    ui->progressBar->hide();
    ui->progtopSpacer->changeSize(0, 0);
    ui->progbottomSpacer->changeSize(0, 0);

    this->installEventFilter(this);
    ui->ioButton->installEventFilter(this);
    ui->doiButton->installEventFilter(this);
    ui->installButton->installEventFilter(this);
    connect(ui->ioButton, &QPushButton::clicked, this, &::MainWindow::Installation_Option);
    connect(ui->doiButton, &QPushButton::clicked, this, &::MainWindow::Installation_Option);
    connect(ui->installButton, &QPushButton::clicked, this, &::MainWindow::Start_Installation);

    downloadWorker = new DownloadWorker(Path, JsonData, this);
    connect(downloadWorker, &DownloadWorker::failed_to_download, this, [this]() {isFailedToDownload = true;});
    connect(downloadWorker, &DownloadWorker::downloadProgress, this, &MainWindow::downloadProgress);
    connect(downloadWorker, &DownloadWorker::finished, this, &MainWindow::Finished_Download);

    installWorker = new InstallWorker(Path, this);
    connect(installWorker, &InstallWorker::failed_to_install, this, [this]() {isFailedToInstall = true;});
    connect(installWorker, &InstallWorker::hide_application, this, &MainWindow::Hide_Application);
    connect(installWorker, &InstallWorker::finished, this, &MainWindow::Finished_Installation);

    Checking_Installer();

    app_tags = {"Access", "Excel", "Lync", "OneNote", "Outlook", "PowerPoint", "Publisher", "Word"};
    for (const QString &app : app_tags) {
        QLabel *label = findChild<QLabel*>(app);
        if (label) {
            label->installEventFilter(this);
        }
    }
}

MainWindow::~MainWindow()
{
    delete ui;
    Stop_Download();
    Stop_Installation();

    if (isSingleInstance) {
        QString toolDir = Path + "/setup.exe";
        if (QFileInfo::exists(toolDir)) {
            QFile::remove(toolDir);
        }

        QString configDir = Path + "/Configuration.xml";
        if (QFileInfo::exists(configDir)) {
            QFile::remove(configDir);
        }
    }
}

void MainWindow::Initialize_Data()
{
    QFile file(":/data/data.json");
    file.open(QIODevice::ReadOnly | QIODevice::Text);
    QByteArray jsonData = file.readAll();
    file.close();
    QJsonParseError error;
    QJsonDocument doc = QJsonDocument::fromJson(jsonData, &error);
    JsonData = doc.object();

    QString bit = JsonData.value("Bit").toString();
    QString buildNo = JsonData.value("BuildNo").toString();

    QJsonArray installerfiles = JsonData.value("Installer_Files").toArray();
    for (int i = 0; i < installerfiles.size(); ++i) {
        QString fileName = installerfiles[i].toString();
        if (fileName.contains("stream")) {
            fileName.replace("{Bit}", Converted_Architecture());
        } else {
            fileName.replace("{Bit}", bit);
        }
        fileName.replace("{BuildNo}", buildNo);
        installerfiles[i] = fileName;
    }

    if (bit == "32") {
        installerfiles << "i640.cab" << "i640.cab.cat" << "i641033.cab";
    }

    JsonData["Installer_Files"] = installerfiles;

    QJsonArray installerfolders = JsonData.value("Installer_Folders").toArray();
    for (int i = 0; i < installerfolders.size(); ++i) {
        QString folderName = installerfolders[i].toString();
        folderName.replace("{BuildNo}", buildNo);
        installerfolders[i] = folderName;
    }

    JsonData["Installer_Folders"] = installerfolders;
}

void MainWindow::Initialize_File()
{
    QFile tool(":/configuration/setup.exe");
    tool.copy(Path + "/setup.exe");

    SetFileAttributes(reinterpret_cast<LPCWSTR>((Path + "/setup.exe").utf16()), FILE_ATTRIBUTE_HIDDEN);

    QString installationFolder = Path + "/Office";
    QDir folderDir(installationFolder);
    if (folderDir.exists()) {
        isAlreadyHaveOffieFolder = true;
    } else {
        isAlreadyHaveOffieFolder = false;
    }
}

QString MainWindow::Converted_Architecture()
{
    QString bit = JsonData.value("Bit").toString();
    if (bit == "32") {
        return "86";
    }
    return "64";
}

void MainWindow::Align_To_Center(int width, int height)
{
    QScreen *primaryScreen = QGuiApplication::primaryScreen();
    QRect availableGeometry = primaryScreen->availableGeometry();

    if (isWindowMove) {
        QSize current_size = this->size();
        QPoint current_position = this->pos();

        int h_size_center = int((current_position.y() + current_size.height() / 2) - (height / 2));
        int w_size_center = int((current_position.x() + current_size.width() / 2) - (width / 2));

        this->setGeometry(w_size_center, h_size_center, width, height);
    } else {
        int center_x = int(availableGeometry.width()/2 - width/2);
        int center_y = int(availableGeometry.height()/2 - height/2);
        this->setGeometry(center_x, center_y, width, height);
    }
}

bool MainWindow::eventFilter(QObject *obj, QEvent *event)
{
    if (obj == ui->CloseButton && event->type() == QEvent::MouseButtonPress) {
        QMouseEvent *mouseEvent = dynamic_cast<QMouseEvent*>(event);
        if (mouseEvent->button() == Qt::LeftButton) {
            qApp->exit();
        }
    }

    if (obj == ui->HeaderGrid) {
        QMouseEvent *mouseEvent = dynamic_cast<QMouseEvent*>(event);
        if (event->type() == QEvent::MouseButtonPress) {
            if (mouseEvent->button() == Qt::LeftButton) {
                oldPos = mouseEvent->globalPosition().toPoint();
                isWindowMove = true;
            }
        }

        if (event->type() == QEvent::MouseMove) {
            QMouseEvent *mouseEvent = dynamic_cast<QMouseEvent*>(event);
            if (!oldPos.isNull()) {
                QPoint delta = mouseEvent->globalPosition().toPoint() - oldPos;
                this->move(this->x() + delta.x(), this->y() + delta.y());
                oldPos = mouseEvent->globalPosition().toPoint();
            }
        }

        if (event->type() == QEvent::MouseButtonRelease) {
            QMouseEvent *mouseEvent = dynamic_cast<QMouseEvent*>(event);
            if (mouseEvent->button() == Qt::LeftButton) {
                oldPos = QPoint();
            }
        }
    }

    if (obj == this) {
        if (event->type() == QEvent::Enter) {
            if (!isDownloading && !isInstalling) {
                Checking_Installer();
            }
        }
    }

    if (obj == ui->ioButton or obj == ui->doiButton or obj == ui->installButton) {
        if ((event->type() == QEvent::Enter && event->type() != QEvent::MouseButtonPress) or
            (event->type() == QEvent::Enter && event->type() != QEvent::MouseButtonRelease) or
            (event->type() == QEvent::Enter && event->type() != QEvent::MouseButtonDblClick)) {
            if (ui->MessageLabel->text() == "Wrong installation folder path."){
                ui->ioButton->setEnabled(false);
                ui->doiButton->setEnabled(false);
            } else {
                ui->ioButton->setEnabled(true);
                ui->doiButton->setEnabled(true);
            }
            if (obj == ui->installButton && Installation_Method != "I̲nstall Online") {
                Checking_Installer();
            } else if (obj == ui->ioButton or obj == ui->doiButton) {
                Checking_Installer();
            }
        }
    }

    if (qobject_cast<QLabel*>(obj) && obj != ui->CloseButton) {
        QLabel *label = qobject_cast<QLabel*>(obj);

        QString border_thickness = label->styleSheet().split(": ")[1].split(" ")[0];

        if (border_thickness == "0px") {
            if (event->type() == QEvent::Enter) {
                label->setMinimumWidth(60);
                label->setMinimumHeight(60);
            } else if (event->type() == QEvent::Leave) {
                label->setMinimumWidth(50);
                label->setMinimumHeight(50);
            }
        }

        if (event->type() == QEvent::MouseButtonPress || event->type() == QEvent::MouseButtonDblClick) {
            QMouseEvent *mouseEvent = static_cast<QMouseEvent*>(event);
            if (mouseEvent->button() == Qt::LeftButton) {
                label->setMinimumWidth(50);
                label->setMinimumHeight(50);
            }
        } else if (event->type() == QEvent::MouseButtonRelease) {
            QMouseEvent *mouseEvent = static_cast<QMouseEvent*>(event);
            if (mouseEvent->button() == Qt::LeftButton) {
                label->setMinimumWidth(60);
                label->setMinimumHeight(60);
                if (border_thickness == "0px") {
                    label->setStyleSheet("border: 1px solid rgb(255, 165, 0);");
                    selected_apps.append(label->objectName());
                    ui->installButton->setEnabled(true);
                } else {
                    label->setStyleSheet("border: 0px solid rgb(255, 165, 0);");
                    selected_apps.removeOne(label->objectName());
                    if (selected_apps.isEmpty()) {
                        ui->installButton->setEnabled(false);
                    }
                }
            }
        }
    }

    return QMainWindow::eventFilter(obj, event);
}

void MainWindow::Installation_Option()
{
    QPushButton *button = qobject_cast<QPushButton *>(sender());

    for (const QString &app: app_tags) {
        QLabel *label = findChild<QLabel*>(app);

        QString border_thickness = label->styleSheet().split(": ")[1].split(" ")[0];
        if( border_thickness == "1px") {
            label->setMinimumWidth(50);
            label->setMinimumHeight(50);
            label->setStyleSheet("border: 0px solid rgb(255, 165, 0);");
        }
    }


    if (button == ui->ioButton) {
        ui->stackedWidget->setCurrentIndex(1);
        Installation_Method = button->text();
        Align_To_Center(500, 400);
        ui->doiButton->setEnabled(false);
        isInstalling = true;
    } else if (button == ui->doiButton) {
        if (button->text() == "Download O̲ffline Installer" or button->text() == "Re-download O̲ffline Installer" or button->text() == "Do̲wnload Again") {
            button->setText("C̲ancel");
            Installation_Method = button->text();
            button->setShortcut(QKeySequence("C"));
            ui->ioButton->setEnabled(false);
            ui->MessageLabel->setStyleSheet("font: 600 24pt 'Segoe UI';"
                                            "color: rgb(95, 95, 95)");
            ui->MessageLabel->setText("Downloading...");
            ui->progressBar->show();
            ui->progtopSpacer->changeSize(20, 15);
            ui->progbottomSpacer->changeSize(20, 20);
            ui->progressBar->setValue(0);
            Align_To_Center(500, 300);
            CreatingConfigFile();
            isCancelDownload = false;
            Start_Download();
        } else {
            Checking_Installer();
            isCancelDownload = true;
            Stop_Download();
        }
    }
}

void MainWindow::Checking_Installer()
{
    CheckInstaller Check(Path, JsonData);

    if (Check.Correct_Path() && Check.File_Size()) {
        ui->stackedWidget->setCurrentIndex(1);
        Align_To_Center(500, 400);
    } else {
        ui->stackedWidget->setCurrentIndex(0);
        ui->ioButton->setText("I̲nstall Online");
        ui->doiButton->setText("Download O̲ffline Installer");

        if (!isFailedToDownload or !isFailedToInstall) {
            if (!Check.Folder() && !Check.File_Size()) {
                ui->MessageLabel->setStyleSheet("font: 600 18pt 'Segoe UI';"
                                                "color: rgb(95, 95, 95)");
                ui->MessageLabel->setText("No installation file was found.");
                ui->doiButton->setText("Download O̲ffline Installer");
                Align_To_Center(500, 230);
            } else if (!Check.Correct_Path() && Check.File_Size()) {
                ui->MessageLabel->setStyleSheet("font: 600 18pt 'Segoe UI';"
                                                "color: rgb(95, 95, 95)");
                ui->MessageLabel->setText("Wrong installation folder path.");
                ui->doiButton->setText("Download O̲ffline Installer");
                Align_To_Center(500, 230);
            } else if (Check.Folder() && !Check.File_Size()) {
                ui->MessageLabel->setStyleSheet("font: 600 18pt 'Segoe UI';"
                                                "color: rgb(95, 95, 95)");
                ui->MessageLabel->setText("Installation file error.");
                ui->doiButton->setText("Re-download O̲ffline Installer");
                Align_To_Center(500, 230);
            }
        }

        if (isFailedToDownload && !isFailedToInstall) {
            ui->MessageLabel->setText("<html><head/><body>"
                                      "<p style='margin: 0;'><span style='font: 600 14pt 'Segoe UI';'>Download failed.</span></p>"
                                      "<p style='margin: 0;'><span style='font: 10pt Segoe UI';'>Please check your internet connection and try again.</span></p>"
                                      "</body></html>");
            ui->doiButton->setText("Do̲wnload Again");
        }

        if (isFailedToInstall && !isFailedToDownload) {
            ui->MessageLabel->setText("<html><head/><body>"
                                      "<p style='margin: 0;'><span style='font: 600 14pt 'Segoe UI';'>Installation failed.</span></p>"
                                      "<p style='margin: 0;'><span style='font: 10pt Segoe UI';'>Please check your internet connection and try again.</span></p>"
                                      "</body></html>");
            ui->ioButton->setText("I̲nstall Online Again");
        }

        ui->doiButton->setShortcut(QKeySequence("O"));
        ui->progressBar->hide();
        ui->progtopSpacer->changeSize(0, 0);
        ui->progbottomSpacer->changeSize(0, 0);
        Align_To_Center(500, 230);
    }
}

void MainWindow::CreatingConfigFile() {
    QFile rawFile(":/configuration/Configuration.xml");
    QFile configFile(Path + "/Configuration.xml");

    rawFile.open(QIODevice::ReadOnly | QIODevice::Text);
    configFile.open(QIODevice::WriteOnly | QIODevice::Text);

    QTextStream out(&configFile);

    QString configContent = rawFile.readAll();

    QStringList configLines = configContent.split("\n");

    QString newOfficeClientEdition = JsonData.value("Bit").toString();
    QString newChannel = JsonData.value("Channel").toString();
    QString newVersion = JsonData.value("BuildNo").toString();
    QString newProductID = JsonData.value("ProductID").toString();

    static QRegularExpression officeClientEditionRegex(R"(OfficeClientEdition="[^"]*")");
    static QRegularExpression channelRegex(R"(Channel="[^"]*")");
    static QRegularExpression versionRegex(R"(Version="[^"]*")");
    static QRegularExpression productIDRegex(R"(ID="[^"]*")");

    for (QString &line : configLines) {
        bool exclude = false;

        if (line.contains("<Add")) {
            line.replace(officeClientEditionRegex,
                         QString("OfficeClientEdition=\"%1\"").arg(newOfficeClientEdition));
            line.replace(channelRegex,
                         QString("Channel=\"%1\"").arg(newChannel));
            line.replace(versionRegex,
                         QString("Version=\"%1\"").arg(newVersion));
        }
        if (line.contains("<Product")) {
            line.replace(productIDRegex,
                         QString("ID=\"%1\"").arg(newProductID));
        }

        for (const QString &app : selected_apps) {
            if (line.contains(QString("<ExcludeApp ID=\"%1\"").arg(app))) {
                exclude = true;
                break;
            }
        }

        if (!exclude) {
            out << line << "\n";
        }
    }

    rawFile.close();
    configFile.close();
    SetFileAttributes(reinterpret_cast<LPCWSTR>((Path + "/Configuration.xml").utf16()), FILE_ATTRIBUTE_HIDDEN);
}

void MainWindow::Start_Download()
{
    isDownloading = true;
    isFailedToDownload = false;
    isFailedToInstall = false;
    ui->ioButton->setEnabled(false);
    ui->ioButton->removeEventFilter(this);
    ui->doiButton->removeEventFilter(this);
    ui->CloseButton->removeEventFilter(this);
    downloadWorker->start();
}

void MainWindow::Stop_Download()
{
    if (downloadWorker->isRunning()) {
        downloadWorker->stop();
        downloadWorker->wait();
    }

    if (isCancelDownload && !isAlreadyHaveOffieFolder) {
        QString installationFolder = Path + "/Office";
        QDir folderDir(installationFolder);
        if (folderDir.exists()) {
            folderDir.removeRecursively();
        }
    }
}

void MainWindow::Finished_Download()
{
    isDownloading = false;
    ui->ioButton->setEnabled(true);
    ui->ioButton->installEventFilter(this);
    ui->doiButton->installEventFilter(this);
    ui->CloseButton->installEventFilter(this);
    Checking_Installer();
}

void MainWindow::downloadProgress(int Progress)
{
    ui->progressBar->setValue(Progress);
    int total_size = JsonData.value("Total_Byte").toInt();
    if (Progress >= total_size * 0.50 ){
        ui->progressBar->setStyleSheet("QProgressBar {"
                                       "   border: 1px solid rgb(95, 95, 95);"
                                       "   border-radius: 0px;"
                                       "   background-color: white;"
                                       "   text-align: center;"
                                       "   color: white;}"
                                       "QProgressBar::chunk {"
                                       "   background-color: qlineargradient("
                                       "   spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
                                       "   rgb(233, 53, 22), stop:1 "
                                       "   rgba(255, 165, 0, 255));"
                                       "   border-radius: 0px;}");
    } else {
        ui->progressBar->setStyleSheet("QProgressBar {"
                                       "   border: 1px solid rgb(95, 95, 95);"
                                       "   border-radius: 0px;"
                                       "   background-color: white;"
                                       "   text-align: center;"
                                       "   color: rgb(95, 95, 95);}"
                                       "QProgressBar::chunk {"
                                       "   background-color: qlineargradient("
                                       "   spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
                                       "   rgb(233, 53, 22), stop:1 "
                                       "   rgba(255, 165, 0, 255));"
                                       "   border-radius: 0px;}");
    }
}

void MainWindow::Start_Installation()
{
    ui->stackedWidget->setCurrentIndex(2);
    ui->progtopSpacer->changeSize(0, 0);
    ui->progbottomSpacer->changeSize(0, 0);
    Align_To_Center(500, 230);
    ui->CloseButton->removeEventFilter(this);
    isInstalling = true;
    isFailedToInstall = false;
    isFailedToDownload = false;
    CreatingConfigFile();
    installWorker->start();
}

void MainWindow::Stop_Installation ()
{
    installWorker->stop();
    installWorker->wait();
}

void MainWindow::Finished_Installation()
{
    isInstalling = false;
    if (isFailedToInstall) {
        ui->ioButton->setEnabled(true);
        ui->doiButton->setEnabled(true);
        ui->CloseButton->installEventFilter(this);
        Checking_Installer();
    } else {
        qApp->exit();
    }
}

void MainWindow::Hide_Application()
{
    this->hide();
}
