#include "downloadworker.h"
#include "calculate_total_byte.h"
#include <Windows.h>

DownloadWorker::DownloadWorker(QString path, QJsonObject jsonData, QObject *parent)
    : QThread(parent), Path(path), JsonData(jsonData)
{
    _isRunning = false;
}

void DownloadWorker::run()
{
    _isRunning = true;
    Process = new QProcess();

    QString tool = Path + "/setup.exe";
    QString config_file = Path + "/Configuration.xml";

    QStringList arguments;
    arguments << "/download" << config_file;
    
    Process->start(tool, arguments);

    Calculate_Total_Byte current_byte(JsonData);
    int total_byte = JsonData.value("Total_Byte").toInt();
    int timeOut = 0;
    int byte = 0;
    while (byte < total_byte)
    {
        if (!_isRunning) {
            Process->kill();
            Process->waitForFinished();
            return;
        }

        if (is_failed_to_Download() or timeOut == 90000){
            emit failed_to_download();
            Process->kill();
            Process->waitForFinished();
            return;
        }

        if (byte == current_byte.Total_Byte()) {
            timeOut += 25;
        } else {
            timeOut = 0;
        }

        emit downloadProgress(byte);
        byte = current_byte.Total_Byte();
        QThread::msleep(10);
    }
}

void DownloadWorker::stop()
{
    _isRunning = false;
}

bool DownloadWorker::is_failed_to_Download()
{
    HWND hWnd = FindWindowW(nullptr, L"Couldn't Install");
    if (hWnd != nullptr) {
        return true;
    }
    return false;
}
