#include "checkinstaller.h"
#include "calculate_total_byte.h"
#include <QCoreApplication>
#include <QDir>
#include <QFileInfo>
#include <QJsonArray>

CheckInstaller::CheckInstaller(QString path, QJsonObject &jsonData)
    : Path(path), JsonData(jsonData)
{
}

bool CheckInstaller::Folder() {
    QString installationFolder = Path + "/Office";
    QDir folderDir(installationFolder);
    if (!folderDir.exists()) {
        return false;
    }
    return true;
}

bool CheckInstaller::File_Size() {
    Calculate_Total_Byte File(Path, JsonData);

    int total_size = JsonData.value("Total_Byte").toInt();
    int size = File.Total_Byte();
    if (size == total_size) {
        return true;
    }
    return false;
}

bool CheckInstaller::Correct_Path() {
    QString buildNo = JsonData.value("BuildNo").toString();
    QString bit = JsonData.value("Bit").toString();
    QJsonArray installerfiles = JsonData.value("Installer_Files").toArray();

    QStringList correctPath;
    for (const QJsonValue &file : installerfiles) {
        if (file.toString() == "v" + bit + "_" + buildNo + ".cab") {
            correctPath.append(Path + "/Office/Data/v" + bit + "_" + buildNo + ".cab");
        } else {
            correctPath.append(Path + "/Office/Data/" + buildNo + "/" + file.toString());
        }
    }

    for (const QString &file : correctPath) {
        if (!QFileInfo::exists(file)) {
            return false;
        }
    }

    return true;
}
