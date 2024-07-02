#ifndef CALCULATE_TOTAL_BYTE_H
#define CALCULATE_TOTAL_BYTE_H
#include <QJsonObject>

class Calculate_Total_Byte
{
public:
    Calculate_Total_Byte(QString path, QJsonObject& jsonData);

    int Total_Byte();
private:
    QString Path;
    QJsonObject JsonData;

    QString Converted_Architecture();
};

#endif // CALCULATE_TOTAL_BYTE_H
