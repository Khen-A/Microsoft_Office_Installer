#include "checkinstaller.h"
#include "calculate_total_byte.h"
#include <QCoreApplication>
#include <QDirIterator>
#include <QDir>
#include <QFileInfo>
#include <QJsonArray>

CheckInstaller::CheckInstaller(const QJsonObject& jsonData)
    : JsonData(jsonData)
{
}

bool CheckInstaller::Folder() {
    QString path = QCoreApplication::applicationDirPath();
    QDirIterator it(path, QDir::Dirs | QDir::NoDotAndDotDot, QDirIterator::Subdirectories);

    QJsonArray installerfolder = JsonData.value("Installer_Folders").toArray();
    QStringList foundFolders;

    while (it.hasNext()) {
        QString subdir = it.next();
        QString name = QFileInfo(subdir).fileName();
        for (const QJsonValue& fname: installerfolder) {
            if (name == fname) {
                foundFolders.append(name);
            }
        }
    }

    for (const QJsonValue &file : installerfolder) {
        if (!foundFolders.contains(file) && !foundFolders.contains("Office")) {
            return false;
        }
    }

    return true;
}

bool CheckInstaller::File_Size() {
    Calculate_Total_Byte File(JsonData);

    int total_size = JsonData.value("Total_Byte").toInt();
    int size = File.Total_Byte();
    if (size == total_size) {
        return true;
    }
    return false;
}

bool CheckInstaller::Correct_Path() {
    QString path = QCoreApplication::applicationDirPath();
    QDirIterator it(path, QDir::Files | QDir::NoDotAndDotDot, QDirIterator::Subdirectories);

    QString BuildNo = JsonData.value("BuildNo").toString();
    QString bit = JsonData.value("Bit").toString();
    QJsonArray installerfiles = JsonData.value("Installer_Files").toArray();

    QStringList correctPath;
    for (const QJsonValue &file : installerfiles) {
        if (file.toString() == "v" + bit + "_" + BuildNo + ".cab") {
            correctPath.append(path + "/Office/Data/v" + bit + "_" + BuildNo + ".cab");
        } else {
            correctPath.append(path + "/Office/Data/" + BuildNo + "/" + file.toString());
        }
    }

    QStringList FilePath;
    while (it.hasNext()) {
        QString subdir = it.next();
        QString name = QFileInfo(subdir).fileName();
        for (const QJsonValue& fname: installerfiles) {
            if (name == fname) {
                FilePath.append(subdir);
            }
        }
    }

    for (const QString &file : correctPath) {
        if (!FilePath.contains(file)) {
            return false;
        }
    }
    return true;
}
