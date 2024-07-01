#ifndef DOWNLOADWORKER_H
#define DOWNLOADWORKER_H

#include <QThread>
#include <QString>
#include <QProcess>
#include <QDebug>
#include <QJsonObject>

class DownloadWorker : public QThread
{
    Q_OBJECT;

public:
    DownloadWorker(QString path, QJsonObject jsonData, QObject *parent = nullptr);

    void stop();

signals:
    void downloadProgress(int Progress);
    void failed_to_download();

protected:
    void run() override;

private:
    bool _isRunning;
    bool is_failed_to_Download();

    QProcess *Process;
    QString Path;
    QJsonObject JsonData;
};

#endif // DOWNLOADWORKER_H
