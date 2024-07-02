#include "calculate_total_byte.h"
#include <QJsonArray>
#include <QFileInfo>
#include <QDirIterator>
#include <QCoreApplication>

Calculate_Total_Byte::Calculate_Total_Byte(QString path, QJsonObject &jsonData)
    : Path(path), JsonData(jsonData)
{
}

int Calculate_Total_Byte::Total_Byte()
{
    int totalSize = 0;
    QJsonArray installerfile = JsonData.value("Installer_Files").toArray();

    QDirIterator it(Path + "/Office", QDir::Files | QDir::NoDotAndDotDot, QDirIterator::Subdirectories);

    while (it.hasNext()) {
        QString file = it.next();
        QString name = QFileInfo(file).fileName();
        if (installerfile.contains(name)) {
            totalSize += QFileInfo(file).size();
        }
    }

    return totalSize;
}
