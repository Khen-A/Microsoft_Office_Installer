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
    QString bit = JsonData.value("bit").toString();
    QStringList installerfile = {"v" + bit + "_16.0.14332.20604.cab",
                                 "i" + bit + "0.cab",
                                 "i" + bit + "0.cab.cat",
                                 "i" + bit + "1033.cab",
                                 "s" + bit + "0.cab",
                                 "s" + bit + "1033.cab",
                                 "stream.x" + bit + ".en-us.dat",
                                 "stream.x" + bit + ".en-us.dat.cat",
                                 "stream.x" + bit + ".x-none.dat",
                                 "stream.x" + bit + ".x-none.dat.cat"};

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
