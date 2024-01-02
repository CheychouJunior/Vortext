# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vortextIlZZAq.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 441)
        MainWindow.setStyleSheet(u"/**#bottomWidget{\n"
"	background-color: #504c4f;\n"
"}**/\n"
"\n"
"#topWidget, #bottomWidget{\n"
"	background-color: #383637;\n"
"}\n"
"\n"
"#videoNameLabel{\n"
"	font-size: 9pt;\n"
"	color: #cecece;\n"
"}\n"
"\n"
"QFrame{\n"
"	border: none;\n"
"}\n"
"\n"
"#openBtn{\n"
"	background-color:#a1239a;\n"
"}\n"
"\n"
"#screenWidget{\n"
"	background-color: #302d33\n"
"}\n"
"\n"
"#toggleBtn{\n"
"	border-radius: 1px\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topWidget = QWidget(self.centralwidget)
        self.topWidget.setObjectName(u"topWidget")
        self.horizontalLayout = QHBoxLayout(self.topWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 4, 3, 4)
        self.frame = QFrame(self.topWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 2, 0, 0)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(20, 20))
        self.logo.setPixmap(QPixmap(u":/icons/logo vortext.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.logo, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_2 = QFrame(self.topWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.videoNameLabel = QLabel(self.frame_2)
        self.videoNameLabel.setObjectName(u"videoNameLabel")
        self.videoNameLabel.setTextFormat(Qt.AutoText)

        self.horizontalLayout_3.addWidget(self.videoNameLabel, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.topWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 3, 3, 0)
        self.reduceBtn = QPushButton(self.frame_3)
        self.reduceBtn.setObjectName(u"reduceBtn")
        icon = QIcon()
        icon.addFile(u":/icons/reduce.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reduceBtn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.reduceBtn)

        self.resizeBtn = QPushButton(self.frame_3)
        self.resizeBtn.setObjectName(u"resizeBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/agrandir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resizeBtn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.resizeBtn)

        self.quitBtn = QPushButton(self.frame_3)
        self.quitBtn.setObjectName(u"quitBtn")
        self.quitBtn.setMaximumSize(QSize(27, 25))

        self.horizontalLayout_2.addWidget(self.quitBtn)


        self.horizontalLayout.addWidget(self.frame_3, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.topWidget)

        self.screenWidget = QWidget(self.centralwidget)
        self.screenWidget.setObjectName(u"screenWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenWidget.sizePolicy().hasHeightForWidth())
        self.screenWidget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.screenWidget)

        self.bottomWidget = QWidget(self.centralwidget)
        self.bottomWidget.setObjectName(u"bottomWidget")
        self.bottomWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.bottomWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.bottomWidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(40, 5, -1, 8)
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 0, 0, 0)
        self.videoSlider = QSlider(self.frame_8)
        self.videoSlider.setObjectName(u"videoSlider")
        self.videoSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.videoSlider)

        self.cur_timeLabel = QLabel(self.frame_8)
        self.cur_timeLabel.setObjectName(u"cur_timeLabel")

        self.horizontalLayout_9.addWidget(self.cur_timeLabel)

        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_9.addWidget(self.label_2)

        self.timeLabel = QLabel(self.frame_8)
        self.timeLabel.setObjectName(u"timeLabel")

        self.horizontalLayout_9.addWidget(self.timeLabel)


        self.horizontalLayout_8.addWidget(self.frame_8)

        self.toggleBtn = QPushButton(self.frame_5)
        self.toggleBtn.setObjectName(u"toggleBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/down arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleBtn.setIcon(icon2)

        self.horizontalLayout_8.addWidget(self.toggleBtn, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_4 = QCustomSlideMenu(self.bottomWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setEnabled(True)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(30, 5, 0, 8)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.openBtn = QPushButton(self.frame_7)
        self.openBtn.setObjectName(u"openBtn")

        self.horizontalLayout_7.addWidget(self.openBtn)

        self.copyBtn = QPushButton(self.frame_7)
        self.copyBtn.setObjectName(u"copyBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.copyBtn.setIcon(icon3)
        self.copyBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.copyBtn)

        self.selectBtn = QPushButton(self.frame_7)
        self.selectBtn.setObjectName(u"selectBtn")

        self.horizontalLayout_7.addWidget(self.selectBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignLeft)

        self.pauseBtn = QPushButton(self.frame_4)
        self.pauseBtn.setObjectName(u"pauseBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseBtn.setIcon(icon4)
        self.pauseBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.pauseBtn, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 30, 0)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(20, 20))
        self.label.setPixmap(QPixmap(u":/icons/volume max.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label)

        self.volumeSlider = QSlider(self.frame_6)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMaximumSize(QSize(250, 16777215))
        self.volumeSlider.setCursor(QCursor(Qt.PointingHandCursor))
        self.volumeSlider.setOrientation(Qt.Horizontal)
        self.volumeSlider.setTickPosition(QSlider.TicksBelow)
        self.volumeSlider.setTickInterval(10)

        self.horizontalLayout_6.addWidget(self.volumeSlider)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignRight)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(15, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.bottomWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VorText Media Player", None))
        self.logo.setText("")
        self.videoNameLabel.setText("")
        self.reduceBtn.setText("")
        self.resizeBtn.setText("")
        self.quitBtn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.cur_timeLabel.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.toggleBtn.setText("")
#if QT_CONFIG(shortcut)
        self.toggleBtn.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.openBtn.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.openBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.copyBtn.setText("")
        self.selectBtn.setText(QCoreApplication.translate("MainWindow", u"select", None))
        self.pauseBtn.setText("")
#if QT_CONFIG(shortcut)
        self.pauseBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText("")
    # retranslateUi

