#include "installworker.h"
#include <Windows.h>

InstallWorker::InstallWorker(QString path, QObject *parent)
    : QThread(parent), Path(path)
{
}

void InstallWorker::run()
{
    _isRunning = true;
    _isAlreadyHide = false;
    Process = new QProcess();

    QString tool = Path + "/setup.exe";
    QString config_file = Path + "/Configuration.xml";

    QStringList arguments;
    arguments << "/configure" << config_file;

    Process->start(tool, arguments);
    while (true) {
        if (!_isRunning) {
            Process->kill();
            Process->waitForFinished();
            return;
        }

        if (!is_Setup_Running()) {
            return;
        }

        if (!_isAlreadyHide) {
            if (is_office_click_to_run_client_running()) {
                emit hide_application();
                _isAlreadyHide = true;
            }
        }

        if (is_failed_to_Install()) {
            emit failed_to_install();
            Process->kill();
            Process->waitForFinished();
            return;
        }
        QThread::msleep(10);
    }

}

void InstallWorker::stop()
{
    _isRunning = false;
}

bool InstallWorker::is_Setup_Running()
{
    QProcess process;
    process.start("tasklist", QStringList() << "/fi" << "imagename eq setup.exe");
    process.waitForFinished();
    QByteArray result = process.readAllStandardOutput();
    QString output(result);

    return output.contains("setup.exe", Qt::CaseInsensitive);
}

bool InstallWorker::is_office_click_to_run_client_running()
{
    HWND hWnd = FindWindowW(nullptr, L"\u202aMicrosoft Office\u202c");
    if (hWnd != nullptr) {
        SetForegroundWindow(hWnd);
        return true;
    }
    return false;
}

bool InstallWorker::is_failed_to_Install()
{
    HWND hWnd = FindWindowW(nullptr, L"Couldn't Install");
    if (hWnd != nullptr) {
        return true;
    }
    return false;
}
