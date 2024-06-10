# This Python file uses the following encoding: utf-8
import os
import shutil
import sys
import subprocess
import ctypes

from PySide6.QtCore import Qt, QPoint, QEvent, QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

ProductID = "ProPlus2021Volume"
BuildNo = "16.0.14332.20604"
bit = "64"

if bit == "32":
    Converted_Architecture = "86"
elif bit == "64":
    Converted_Architecture = bit

BaseDirectory = os.path.dirname(os.path.abspath(__file__))
installer_file = [f"v{bit}_16.0.14332.20604.cab", f"i{bit}0.cab", f"i{bit}0.cab.cat", f"i{bit}1033.cab", f"s{bit}0.cab",
                  f"s{bit}1033.cab", f"stream.x{bit}.en-us.dat", f"stream.x{bit}.en-us.dat.cat",
                  f"stream.x{bit}.x-none.dat", f"stream.x{bit}.x-none.dat.cat"]
installer_folder = ["Office", "Data", "16.0.14332.20604"]
total_byte = 1941706985
installation_method = ""

selected_apps = []


class SelectionWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.align_to_Center(500, 300)

        self.old_pos = None
        self.installer_folder_path = os.path.join(BaseDirectory, installer_folder[0])
        self.config_file = os.path.join(BaseDirectory, f"Configuration-x{Converted_Architecture}.xml")
        self.temp_file = os.path.join(BaseDirectory, f"Temporary-x{Converted_Architecture}.xml")

        self.download_worker = DownloadWorker()
        self.download_worker.download_progress.connect(self.update_progress_bar)
        self.download_worker.finished.connect(self.finished_download)
        self.installation_worker = InstallationWorker()
        self.installation_worker.hide_application.connect(self.hide)
        self.installation_worker.finished.connect(self.finished_installation)

        self.ui.HeaderGrid.mousePressEvent = self.start_position
        self.ui.HeaderGrid.mouseMoveEvent = self.move_window
        self.ui.HeaderGrid.mouseReleaseEvent = self.stop_position

        self.ui.CloseButton.mousePressEvent = self.exit

        self.ui.ProductIDLabel.setText(ProductID)
        self.ui.VersionLabel.setText(f"v{BuildNo}")

        self.ui.ArchitectureLabel.setText(f"x{Converted_Architecture}")

        self.ui.progressBar.setMaximum(total_byte)

        self.ui.diButton.clicked.connect(lambda: self.download(self.ui.diButton))
        self.ui.doiButton.clicked.connect(lambda: self.download(self.ui.doiButton))
        self.ui.installButton.clicked.connect(lambda: self.start_installation())

        self.app_tags = ["Access", "Excel", "Lync", "OneDrive", "OneNote", "Outlook", "PowerPoint", "Publisher", "Word"]

        for app in self.app_tags:
            label = getattr(self.ui, app)
            label.installEventFilter(self)

        self.checking_installer()

    def start_position(self, event):
        self.old_pos = event.globalPosition().toPoint()

    def move_window(self, event):
        if self.old_pos:
            delta = QPoint(event.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def stop_position(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = None

    def exit(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.close()

    def eventFilter(self, source, event):
        if isinstance(source, QLabel):
            border_thickness = source.styleSheet().split(": ")[1].split(" ")[0]
            if border_thickness == "0px":
                if event.type() == QEvent.Type.Enter:
                    source.setMinimumWidth(60)
                    source.setMinimumHeight(60)
                elif event.type() == QEvent.Type.Leave:
                    source.setMinimumWidth(50)
                    source.setMinimumHeight(50)

            if event.type() == QEvent.Type.MouseButtonPress or event.type() == QEvent.Type.MouseButtonDblClick:
                if event.button() == Qt.MouseButton.LeftButton:
                    source.setMinimumWidth(50)
                    source.setMinimumHeight(50)
            elif event.type() == QEvent.Type.MouseButtonRelease:
                if event.button() == Qt.MouseButton.LeftButton:
                    source.setMinimumWidth(60)
                    source.setMinimumHeight(60)
                    if border_thickness == "0px":
                        source.setStyleSheet("border: 1px solid rgb(255, 165, 0);")
                        selected_apps.append(source.objectName())
                        self.ui.installButton.setEnabled(True)
                        print(selected_apps)
                    else:
                        source.setStyleSheet("border: 0px solid rgb(255, 165, 0);")
                        selected_apps.remove(source.objectName())
                        if len(selected_apps) == 0:
                            self.ui.installButton.setEnabled(False)
        return super().eventFilter(source, event)

    def align_to_Center(self, width: int, height: int):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        center_x = int(screen_geometry.width()/2 - width/2)
        center_y = int(screen_geometry.height()/2 - height/2)
        self.setGeometry(center_x, center_y, width, height)

    def align_to_CenterApplication(self, width: int, height: int):
        current_size = self.size()
        current_position = self.pos()

        h_size_center = int((current_position.y() + current_size.height() / 2) - (height / 2))
        w_size_center = int((current_position.x() + current_size.width() / 2) - (width / 2))

        self.setGeometry(w_size_center, h_size_center, width, height)

    def checking_installer(self):
        if CheckInstaller().folder() and CheckInstaller().file():
            self.ui.stackedWidget.setCurrentIndex(1)
            self.align_to_CenterApplication(500, 400)
            return
        elif not CheckInstaller().folder() and not CheckInstaller().file():
            self.ui.MessageLabel.setText("No installation file was found.")
            self.ui.doiButton.setText("Download O̲ffline Installer")

        elif not CheckInstaller().folder() and CheckInstaller().file():
            self.ui.MessageLabel.setText("Wrong installation folder path.")
            self.ui.doiButton.setText("Re-download O̲ffline Installer")

        elif CheckInstaller().folder() and not CheckInstaller().file():
            self.ui.MessageLabel.setText("Installation file error.")
            self.ui.doiButton.setText("Re-download O̲ffline Installer")

        self.ui.doiButton.setShortcut("O")
        self.ui.progressBar.hide()
        self.ui.progtopSpacer.changeSize(0, 0)
        self.ui.progbottomSpacer.changeSize(0, 0)
        self.align_to_CenterApplication(500, 230)

    def download(self, source: QPushButton):
        global installation_method
        installation = ""

        for app in self.app_tags:
            label = getattr(self.ui, app)
            border_thickness = label.styleSheet().split(": ")[1].split(" ")[0]
            if border_thickness == "1px":
                label.setMinimumWidth(50)
                label.setMinimumHeight(50)
                label.setStyleSheet("border: 0px solid rgb(255, 165, 0);")
        selected_apps.clear()

        if source == self.ui.diButton:
            installation = source.text()
            installation_method = source.text()
        elif source == self.ui.doiButton:
            installation = source.text()
            installation_method = source.text()

        if installation == "I̲nstall Online":
            self.ui.stackedWidget.setCurrentIndex(1)
            self.align_to_CenterApplication(500, 400)
        elif installation == "Download O̲ffline Installer" or installation == "Re-download O̲ffline Installer":
            source.setText("C̲ancel")
            source.setShortcut("C")
            self.ui.diButton.setEnabled(False)
            self.ui.MessageLabel.setText("Downloading...")
            self.ui.progressBar.show()
            self.ui.progtopSpacer.changeSize(20, 15)
            self.ui.progbottomSpacer.changeSize(20, 20)
            self.ui.progressBar.setValue(0)
            self.align_to_CenterApplication(500, 300)
            self.start_download()
        if installation == "C̲ancel":
            self.cancel_download()
            source.setShortcut("O")
            self.checking_installer()

    def start_download(self):
        self.download_worker.start()

    def cancel_download(self):
        if self.download_worker.isRunning():
            self.download_worker.stop()
            self.download_worker.wait()

        if CheckInstaller().folder():
            self.delete_installer_folder()

    def finished_download(self):
        self.checking_installer()
        self.ui.diButton.setEnabled(True)

    def update_progress_bar(self, value):
        self.ui.progressBar.setValue(value)
        if value >= total_byte * 0.53:
            self.ui.progressBar.setStyleSheet("QProgressBar {"
                                              "   border: 1px solid rgb(95, 95, 95);"
                                              "   border-radius: 0px;"
                                              "   background-color: white;"
                                              "   text-align: center;"
                                              "   color: white;}"
                                              "QProgressBar::chunk {"
                                              "   background-color: qlineargradient("
                                              "   spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
                                              "   rgb(233, 53, 22), stop:1 "
                                              "   rgba(255, 165, 0, 255));"
                                              "   border-radius: 0px;}")
        else:
            self.ui.progressBar.setStyleSheet("QProgressBar {"
                                              "   border: 1px solid rgb(95, 95, 95);"
                                              "   border-radius: 0px;"
                                              "   background-color: white;"
                                              "   text-align: center;"
                                              "   color: rgb(95, 95, 95);}"
                                              "QProgressBar::chunk {"
                                              "   background-color: qlineargradient("
                                              "   spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
                                              "   rgb(233, 53, 22), stop:1 "
                                              "   rgba(255, 165, 0, 255));"
                                              "   border-radius: 0px;}")

    def delete_installer_folder(self):
        if os.path.isdir(self.installer_folder_path):
            shutil.rmtree(self.installer_folder_path)

    def start_installation(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.progtopSpacer.changeSize(0, 0)
        self.ui.progbottomSpacer.changeSize(0, 0)
        self.align_to_CenterApplication(500, 230)
        self.ui.CloseButton.setEnabled(False)
        self.run_configuration_file()

    def finished_installation(self):
        if is_failed_to_download_or_install():
            self.checking_installer()
            if installation_method == "I̲nstall Online":
                self.ui.stackedWidget.setCurrentIndex(0)
                self.align_to_CenterApplication(500, 230)
            self.ui.CloseButton.setEnabled(True)
        else:
            os.remove(self.temp_file)
            self.close()
            sys.exit()

    def run_configuration_file(self):
        shutil.copy(self.config_file, self.temp_file)

        with open(self.config_file, 'r') as tf:
            lines = tf.readlines()
        with open(self.temp_file, 'w') as tft:
            for line in lines:
                if not any(f'<ExcludeApp ID="{app}"' in line for app in selected_apps):
                    tft.write(line)

        self.installation_worker.start()


class DownloadWorker(QThread):
    download_progress = Signal(int)

    def __init__(self):
        super().__init__()
        self._is_running = False

    def run(self):
        current_byte = 0
        self._is_running = True

        tool = "DeploymentTool.exe"
        command = [f"{tool}", "/download", f"Temporary-x{Converted_Architecture}.xml"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        while current_byte < total_byte:
            if not self._is_running:
                subprocess.run(['taskkill', '/F', '/IM', tool])
                process.wait()
                return

            if is_failed_to_download_or_install():
                return

            current_byte = calculate_total_byte(installer_file)
            self.download_progress.emit(current_byte)

    def stop(self):
        self._is_running = False


class InstallationWorker(QThread):
    hide_application = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        command = ["DeploymentTool.exe", "/configure", f"Temporary-x{Converted_Architecture}.xml"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        while True:
            if is_office_click_to_run_client_running():
                self.hide_application.emit()
                break

            if is_failed_to_download_or_install():
                return
        process.wait()


class CheckInstaller:
    def __init__(self):
        self._folder = False
        self._file = False

    def folder(self):
        found_folder = []
        for root, dirs, files in os.walk(BaseDirectory):
            for x in dirs:
                found_folder.append(x)

        for _folder_ in installer_folder:
            if _folder_ in found_folder:
                self._folder = True
            else:
                self._folder = False
                break
        return self._folder

    def file(self):
        current_byte = calculate_total_byte(installer_file)
        if current_byte == total_byte:
            self._file = True
        else:
            self._file = False
        return self._file


def run_as_administrator():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, os.path.basename(__file__), None, 1)
        sys.exit()


def is_single_instance(_title):
    lpctstr = ctypes.c_wchar_p

    if not is_office_click_to_run_client_running():
        mutex_handle = ctypes.windll.kernel32.CreateMutexW(None, True, lpctstr(_title))

        if ctypes.windll.kernel32.GetLastError() == 183 or mutex_handle is None:

            hwnd = ctypes.windll.user32.FindWindowW(None, lpctstr(_title))

            if hwnd != 0:
                ctypes.windll.user32.ShowWindow(hwnd, 1)
                ctypes.windll.user32.SetForegroundWindow(hwnd)
            return False
        return True
    else:
        return False


def is_failed_to_download_or_install():
    lpctstr = ctypes.c_wchar_p
    hwnd = ctypes.windll.user32.FindWindowW(None, lpctstr("Couldn't Install"))
    if hwnd != 0:
        ctypes.windll.user32.SetForegroundWindow(hwnd)
        return True
    else:
        return False


def is_office_click_to_run_client_running():
    lpctstr = ctypes.c_wchar_p
    hwnd = ctypes.windll.user32.FindWindowW(None, lpctstr("\u202aMicrosoft Office\u202c"))
    if hwnd != 0:
        ctypes.windll.user32.SetForegroundWindow(hwnd)
        return True
    else:
        return False


def calculate_total_byte(files):
    current_byte = 0
    for root, dirs, filenames in os.walk(BaseDirectory):
        for filename in filenames:
            if filename in files:
                file_path = os.path.join(root, filename)
                current_byte += os.path.getsize(file_path)
    return current_byte


if __name__ == "__main__":
    application = QApplication(sys.argv)
    widget = SelectionWindow()
    window_title = widget.windowTitle()

    run_as_administrator()
    if not is_single_instance(window_title):
        sys.exit()

    widget.show()
    sys.exit(application.exec())
