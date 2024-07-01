#include "mainwindow.h"

#include <QApplication>
#include <QLocale>
#include <Windows.h>
#include <QTranslator>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;

    std::wstring title = w.windowTitle().toStdWString();
    const wchar_t* apptitle = title.c_str();

    HWND hWnd = FindWindow(nullptr, apptitle);
    if (hWnd) {
        bool isMaximized = IsZoomed(hWnd) != 0;

        if (isMaximized) {
            ShowWindow(hWnd, SW_MAXIMIZE);
        } else {
            ShowWindow(hWnd, SW_RESTORE);
        }
        SetForegroundWindow(hWnd);
        w.isSingleInstance = false;
        return 0;
    } else {
        w.isSingleInstance = true;
    }

    QTranslator translator;
    const QStringList uiLanguages = QLocale::system().uiLanguages();
    for (const QString &locale : uiLanguages) {
        const QString baseName = "Microsoft_Office_Installer_" + QLocale(locale).name();
        if (translator.load(":/i18n/" + baseName)) {
            a.installTranslator(&translator);
            break;
        }
    }

    w.setWindowFlags(Qt::FramelessWindowHint);
    w.show();
    return a.exec();
}
