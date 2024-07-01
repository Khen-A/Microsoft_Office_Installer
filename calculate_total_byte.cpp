#include "calculate_total_byte.h"
#include <QJsonArray>
#include <QFileInfo>
#include <QDirIterator>
#include <QCoreApplication>

Calculate_Total_Byte::Calculate_Total_Byte(const QJsonObject& jsonData)
    : JsonData(jsonData)
{
}


int Calculate_Total_Byte::Total_Byte()
{
    int totalSize = 0;
    QJsonArray installerfile = JsonData.value("Installer_Files").toArray();

    QString path = QCoreApplication::applicationDirPath();
    QDirIterator it(path, QDir::Files | QDir::NoDotAndDotDot, QDirIterator::Subdirectories);

    while (it.hasNext()) {
        QString file = it.next();
        QString name = QFileInfo(file).fileName();
        if (installerfile.contains(name)) {
            totalSize += QFileInfo(file).size();
        }
    }

    return totalSize;
}
