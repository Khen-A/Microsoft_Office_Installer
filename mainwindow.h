#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "downloadworker.h"
#include "installworker.h"
#include <QMainWindow>
#include <QJsonObject>
#include <QProgressBar>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

    QJsonObject JsonData;
private slots:
    void downloadProgress(int Progress);
    void Hide_Application();

private:
    Ui::MainWindow *ui;

    void Initialize_Data();
    void Initialize_File();
    void Align_To_Center(int width, int height);
    void Installation_Option();
    void Checking_Installer();
    void CreatingConfigFile();
    void Start_Download();
    void Stop_Download();
    void Finished_Download();
    void Start_Installation();
    void Stop_Installation();
    void Finished_Installation();

    bool eventFilter(QObject *obj, QEvent *event);
    bool isWindowMove;
    bool isAlreadyHaveOffieFolder;
    bool isDownloading;
    bool isCancelDownload;
    bool isFailedToDownload;
    bool isInstalling;
    bool isFailedToInstall;

    DownloadWorker *downloadWorker;
    InstallWorker *installWorker;
    QString Path;
    QPoint oldPos;
    QString Converted_Architecture();
    QStringList app_tags;
    QStringList selected_apps;
    QString Installation_Method;
};
#endif // MAINWINDOW_H
