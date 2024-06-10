# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 300)
        MainWindow.setMinimumSize(QSize(500, 200))
        MainWindow.setMaximumSize(QSize(500, 400))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"#centralwidget {background: white}\n"
"#mainframe  {\n"
"	border: 1px solid rgb(233, 53, 22);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.mainframe = QFrame(self.centralwidget)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setStyleSheet(u"")
        self.mainframe.setFrameShape(QFrame.Box)
        self.mainframe.setFrameShadow(QFrame.Plain)
        self.mainframe.setLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.mainframe)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.FooterGrid = QWidget(self.mainframe)
        self.FooterGrid.setObjectName(u"FooterGrid")
        self.FooterGrid.setMinimumSize(QSize(0, 30))
        self.FooterGrid.setMaximumSize(QSize(16777215, 30))
        self.FooterGrid.setStyleSheet(u"QLabel {\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(95, 95, 95)\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.FooterGrid)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.ProductIDLabel = QLabel(self.FooterGrid)
        self.ProductIDLabel.setObjectName(u"ProductIDLabel")

        self.horizontalLayout_4.addWidget(self.ProductIDLabel)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.VersionLabel = QLabel(self.FooterGrid)
        self.VersionLabel.setObjectName(u"VersionLabel")

        self.horizontalLayout_4.addWidget(self.VersionLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.ArchitectureLabel = QLabel(self.FooterGrid)
        self.ArchitectureLabel.setObjectName(u"ArchitectureLabel")

        self.horizontalLayout_4.addWidget(self.ArchitectureLabel)


        self.gridLayout_3.addWidget(self.FooterGrid, 3, 0, 1, 1)

        self.HeaderGrid = QWidget(self.mainframe)
        self.HeaderGrid.setObjectName(u"HeaderGrid")
        self.HeaderGrid.setMinimumSize(QSize(0, 30))
        self.HeaderGrid.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.HeaderGrid, 0, 0, 1, 1)

        self.TitleGrid = QWidget(self.mainframe)
        self.TitleGrid.setObjectName(u"TitleGrid")
        self.TitleGrid.setMinimumSize(QSize(0, 45))
        self.TitleGrid.setMaximumSize(QSize(16777215, 45))
        self.gridLayout_9 = QGridLayout(self.TitleGrid)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.TitleGrid)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_7 = QGridLayout(self.widget_2)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(25, 0, 0, 0)
        self.Logo = QLabel(self.widget_2)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setEnabled(True)
        self.Logo.setMinimumSize(QSize(153, 33))
        self.Logo.setMaximumSize(QSize(153, 33))
        self.Logo.setStyleSheet(u"")
        self.Logo.setLineWidth(0)
        self.Logo.setPixmap(QPixmap(u":/icon/Image_Resources/logo.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Logo.setIndent(0)

        self.gridLayout_7.addWidget(self.Logo, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_2, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(254, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.widget = QWidget(self.TitleGrid)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.gridLayout_8 = QGridLayout(self.widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, 0, 25, 40)
        self.CloseButton = QLabel(self.widget)
        self.CloseButton.setObjectName(u"CloseButton")
        self.CloseButton.setEnabled(True)
        self.CloseButton.setMinimumSize(QSize(15, 15))
        self.CloseButton.setMaximumSize(QSize(15, 15))
        self.CloseButton.setLayoutDirection(Qt.LeftToRight)
        self.CloseButton.setStyleSheet(u"")
        self.CloseButton.setLineWidth(0)
        self.CloseButton.setPixmap(QPixmap(u":/icon/Image_Resources/close.png"))
        self.CloseButton.setScaledContents(True)
        self.CloseButton.setAlignment(Qt.AlignCenter)
        self.CloseButton.setIndent(0)

        self.gridLayout_8.addWidget(self.CloseButton, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.widget, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.TitleGrid, 1, 0, 1, 1)

        self.BodyGrid = QWidget(self.mainframe)
        self.BodyGrid.setObjectName(u"BodyGrid")
        self.BodyGrid.setMaximumSize(QSize(16777215, 16777215))
        self.BodyGrid.setAutoFillBackground(False)
        self.gridLayout_4 = QGridLayout(self.BodyGrid)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.BodyGrid)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"#page {\n"
"	background-color: white;\n"
"}\n"
"\n"
"#page_2 {\n"
"	background-color: white;\n"
"}")
        self.DownloadPage = QWidget()
        self.DownloadPage.setObjectName(u"DownloadPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DownloadPage.sizePolicy().hasHeightForWidth())
        self.DownloadPage.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.DownloadPage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.MessageLabel = QLabel(self.DownloadPage)
        self.MessageLabel.setObjectName(u"MessageLabel")
        self.MessageLabel.setStyleSheet(u"font: 600 24pt \"Segoe UI\";\n"
"color: rgb(95, 95, 95)")
        self.MessageLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.MessageLabel, 0, Qt.AlignHCenter)

        self.progtopSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.progtopSpacer)

        self.progressBar = QProgressBar(self.DownloadPage)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(300, 0))
        self.progressBar.setMaximumSize(QSize(16777215, 20))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	border: 1px solid rgb(95, 95, 95);\n"
"	border-radius: 0px;\n"
"	background-color: white;\n"
"	text-align: center;\n"
"    color: rgb(95, 95, 95);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(233, 53, 22), stop:1 rgba(255, 165, 0, 255));\n"
"	border-radius: 0px;\n"
"}")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(50)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_3.addWidget(self.progressBar, 0, Qt.AlignHCenter)

        self.progbottomSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.progbottomSpacer)

        self.widget_7 = QWidget(self.DownloadPage)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid black;\n"
"	font: 600 9pt \"Segoe UI\";\n"
"	color: rgb(95, 95, 95)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid black;\n"
"	color: rgb(95, 95, 95);\n"
"	background-color: rgb(205, 230, 247)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 1px solid black;\n"
"	color: rgb(95, 95, 95);\n"
"	background-color: rgb(146, 192, 224)\n"
"}")
        self.gridLayout_5 = QGridLayout(self.widget_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(60)
        self.gridLayout_5.setVerticalSpacing(6)
        self.diButton = QPushButton(self.widget_7)
        self.diButton.setObjectName(u"diButton")
        self.diButton.setEnabled(True)
        self.diButton.setMinimumSize(QSize(150, 30))
        self.diButton.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout_5.addWidget(self.diButton, 0, 0, 1, 1)

        self.doiButton = QPushButton(self.widget_7)
        self.doiButton.setObjectName(u"doiButton")
        self.doiButton.setMinimumSize(QSize(150, 30))
        self.doiButton.setCursor(QCursor(Qt.ArrowCursor))
        self.doiButton.setCheckable(False)
        self.doiButton.setFlat(False)

        self.gridLayout_5.addWidget(self.doiButton, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_7, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.stackedWidget.addWidget(self.DownloadPage)
        self.SelectionPage = QWidget()
        self.SelectionPage.setObjectName(u"SelectionPage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SelectionPage.sizePolicy().hasHeightForWidth())
        self.SelectionPage.setSizePolicy(sizePolicy1)
        self.SelectionPage.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid black;\n"
"	text-align: center;\n"
"	font: 600 9pt \"Segoe UI\";\n"
"	color: rgb(95, 95, 95)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid black;\n"
"	color: rgb(95, 95, 95);\n"
"	background-color: rgb(205, 230, 247)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 1px solid black;\n"
"	color: rgb(95, 95, 95);\n"
"	background-color: rgb(146, 192, 224)\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.SelectionPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.appbutton = QWidget(self.SelectionPage)
        self.appbutton.setObjectName(u"appbutton")
        self.appbutton.setMinimumSize(QSize(300, 200))
        self.appbutton.setMaximumSize(QSize(250, 200))
        self.appbutton.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.appbutton)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.app1 = QWidget(self.appbutton)
        self.app1.setObjectName(u"app1")
        self.app1.setMinimumSize(QSize(195, 0))
        self.app1.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.app1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Access = QLabel(self.app1)
        self.Access.setObjectName(u"Access")
        self.Access.setEnabled(True)
        self.Access.setMinimumSize(QSize(50, 50))
        self.Access.setMaximumSize(QSize(50, 50))
        self.Access.setStyleSheet(u"border: 0px solid rgb(255, 165, 0);")
        self.Access.setPixmap(QPixmap(u":/icon/Image_Resources/access.png"))
        self.Access.setScaledContents(True)
        self.Access.setAlignment(Qt.AlignCenter)
        self.Access.setIndent(-1)

        self.horizontalLayout.addWidget(self.Access, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.Excel = QLabel(self.app1)
        self.Excel.setObjectName(u"Excel")
        self.Excel.setMinimumSize(QSize(50, 50))
        self.Excel.setMaximumSize(QSize(50, 50))
        self.Excel.setStyleSheet(u"border: 0px solid rgb(255, 165, 0);")
        self.Excel.setPixmap(QPixmap(u":/icon/Image_Resources/excel.png"))
        self.Excel.setScaledContents(True)
        self.Excel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Excel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.Lync = QLabel(self.app1)
        self.Lync.setObjectName(u"Lync")
        self.Lync.setMinimumSize(QSize(50, 50))
        self.Lync.setMaximumSize(QSize(50, 50))
        self.Lync.setStyleSheet(u"border: 0px solid rgb(255, 165, 0);")
        self.Lync.setFrameShadow(QFrame.Plain)
        self.Lync.setPixmap(QPixmap(u":/icon/Image_Resources/onedrive.png"))
        self.Lync.setScaledContents(True)
        self.Lync.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Lync, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.app1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.app2 = QWidget(self.appbutton)
        self.app2.setObjectName(u"app2")
        self.app2.setMinimumSize(QSize(260, 0))
        self.app2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.app2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.OneDrive = QLabel(self.app2)
        self.OneDrive.setObjectName(u"OneDrive")
        self.OneDrive.setMinimumSize(QSize(50, 50))
        self.OneDrive.setMaximumSize(QSize(50, 50))
        self.OneDrive.setStyleSheet(u"border: 0px solid rgb(255, 165, 0);")
        self.OneDrive.setPixmap(QPixmap(u":/icon/Image_Resources/onenote.png"))
        self.OneDrive.setScaledContents(True)
        self.OneDrive.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.OneDrive, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.OneNote = QLabel(self.app2)
        self.OneNote.setObjectName(u"OneNote")
        self.OneNote.setMinimumSize(QSize(50, 50))
        self.OneNote.setMaximumSize(QSize(50, 50))
        self.OneNote.setStyleSheet(u"border: 0px solid rgb(255, 165, 0);")
        self.OneNote.setPixmap(QPixmap(u":/icon/Image_Resources/outlook.png"))
        self.OneNote.setScaledContents(True)
        self.OneNote.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.OneNote, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.Outlook = QLabel(self.app2)
        self.Outlook.setObjectName(u"Outlook")
        self.Outlook.setMinimumSize(QSize(50, 50))
        self.Outlook.setMaximumSize(QSize(50, 50))
        self.Outlook.setStyleSheet(u"border: 0px solid rgb(255, 165, 0);")
        self.Outlook.setPixmap(QPixmap(u":/icon/Image_Resources/powerpoint.png"))
        self.Outlook.setScaledContents(True)
        self.Outlook.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Outlook, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.PowerPoint = QLabel(self.app2)
        self.PowerPoint.setObjectName(u"PowerPoint")
        self.PowerPoint.setMinimumSize(QSize(50, 50))
        self.PowerPoint.setMaximumSize(QSize(50, 50))
        self.PowerPoint.setStyleSheet(u"border: 0px solid rgb(255, 165, 0);")
        self.PowerPoint.setPixmap(QPixmap(u":/icon/Image_Resources/publisher.png"))
        self.PowerPoint.setScaledContents(True)
        self.PowerPoint.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.PowerPoint, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.app2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.app3 = QWidget(self.appbutton)
        self.app3.setObjectName(u"app3")
        self.app3.setMinimumSize(QSize(130, 0))
        self.app3.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.app3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Publisher = QLabel(self.app3)
        self.Publisher.setObjectName(u"Publisher")
        self.Publisher.setMinimumSize(QSize(50, 50))
        self.Publisher.setMaximumSize(QSize(50, 50))
        self.Publisher.setStyleSheet(u"border: 0px solid rgb(255, 165, 0);")
        self.Publisher.setPixmap(QPixmap(u":/icon/Image_Resources/skype.png"))
        self.Publisher.setScaledContents(True)
        self.Publisher.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Publisher, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.Word = QLabel(self.app3)
        self.Word.setObjectName(u"Word")
        self.Word.setMinimumSize(QSize(50, 50))
        self.Word.setMaximumSize(QSize(50, 50))
        self.Word.setStyleSheet(u"border: 0px solid rgb(255, 165, 0);")
        self.Word.setPixmap(QPixmap(u":/icon/Image_Resources/word.png"))
        self.Word.setScaledContents(True)
        self.Word.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Word, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.app3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.appbutton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.installButton = QPushButton(self.SelectionPage)
        self.installButton.setObjectName(u"installButton")
        self.installButton.setEnabled(False)
        self.installButton.setMinimumSize(QSize(110, 30))
        self.installButton.setMaximumSize(QSize(110, 30))
        self.installButton.setLayoutDirection(Qt.LeftToRight)
        self.installButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.installButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.SelectionPage)
        self.proccessPage = QWidget()
        self.proccessPage.setObjectName(u"proccessPage")
        self.verticalLayout_4 = QVBoxLayout(self.proccessPage)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)

        self.TextLabel = QLabel(self.proccessPage)
        self.TextLabel.setObjectName(u"TextLabel")
        self.TextLabel.setMaximumSize(QSize(16777215, 50))
        self.TextLabel.setStyleSheet(u"font: 600 24pt \"Segoe UI\";\n"
"color: rgb(95, 95, 95)")
        self.TextLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.TextLabel)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.TextLabel_2 = QLabel(self.proccessPage)
        self.TextLabel_2.setObjectName(u"TextLabel_2")
        self.TextLabel_2.setMinimumSize(QSize(0, 0))
        self.TextLabel_2.setMaximumSize(QSize(16777215, 30))
        self.TextLabel_2.setStyleSheet(u"font:  12pt \"Segoe UI\";\n"
"color: rgb(95, 95, 95)")
        self.TextLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.TextLabel_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.stackedWidget.addWidget(self.proccessPage)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.BodyGrid, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.mainframe, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SelectionWindow", None))
        self.ProductIDLabel.setText(QCoreApplication.translate("MainWindow", u"ProductID", None))
        self.VersionLabel.setText(QCoreApplication.translate("MainWindow", u"version", None))
        self.ArchitectureLabel.setText(QCoreApplication.translate("MainWindow", u"Architecture", None))
        self.Logo.setText("")
        self.CloseButton.setText("")
        self.MessageLabel.setText(QCoreApplication.translate("MainWindow", u"Downloading....", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.diButton.setText(QCoreApplication.translate("MainWindow", u"I\u0332nstall Online", None))
#if QT_CONFIG(shortcut)
        self.diButton.setShortcut(QCoreApplication.translate("MainWindow", u"I", None))
#endif // QT_CONFIG(shortcut)
        self.doiButton.setText(QCoreApplication.translate("MainWindow", u"Download O\u0332ffline Installer", None))
#if QT_CONFIG(shortcut)
        self.doiButton.setShortcut(QCoreApplication.translate("MainWindow", u"O", None))
#endif // QT_CONFIG(shortcut)
        self.Access.setText("")
        self.Excel.setText("")
        self.Lync.setText("")
        self.OneDrive.setText("")
        self.OneNote.setText("")
        self.Outlook.setText("")
        self.PowerPoint.setText("")
        self.Publisher.setText("")
        self.Word.setText("")
        self.installButton.setText(QCoreApplication.translate("MainWindow", u"I\u0332nstall", None))
#if QT_CONFIG(shortcut)
        self.installButton.setShortcut(QCoreApplication.translate("MainWindow", u"I", None))
#endif // QT_CONFIG(shortcut)
        self.TextLabel.setText(QCoreApplication.translate("MainWindow", u"Preparing installation...", None))
        self.TextLabel_2.setText(QCoreApplication.translate("MainWindow", u"This may take a moment.", None))
    # retranslateUi

