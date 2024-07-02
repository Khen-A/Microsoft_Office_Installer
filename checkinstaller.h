#ifndef CHECKINSTALLER_H
#define CHECKINSTALLER_H
#include <QJsonObject>

class CheckInstaller
{
public:
    CheckInstaller(QString path, QJsonObject& jsonData);

    bool Folder();
    bool File_Size();
    bool Correct_Path();
private:
    QString Path;
    QJsonObject JsonData;
};

#endif // CHECKINSTALLER_H
