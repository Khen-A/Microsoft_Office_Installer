#ifndef INSTALLWORKER_H
#define INSTALLWORKER_H

#include <QThread>
#include <QProcess>
#include <QJsonObject>

class InstallWorker : public QThread
{
    Q_OBJECT;

public:
    InstallWorker(QString path, QObject *parent = nullptr);

    void stop();

signals:
    void hide_application();
    void failed_to_install();

protected:
    void run() override;

private:
    bool _isRunning;
    bool _isAlreadyHide;
    bool is_Setup_Running();
    bool is_office_click_to_run_client_running();
    bool is_failed_to_Install();

    QProcess *Process;
    QString Path;
};

#endif // INSTALLWORKER_H
