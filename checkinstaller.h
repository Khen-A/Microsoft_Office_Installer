#ifndef CHECKINSTALLER_H
#define CHECKINSTALLER_H
#include <QJsonObject>

class CheckInstaller
{
public:
    CheckInstaller(const QJsonObject& jsonData);

    bool Folder();
    bool File_Size();
    bool Correct_Path();
private:
    QJsonObject JsonData;
};

#endif // CHECKINSTALLER_H
