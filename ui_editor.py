# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editorIfsDMh.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 441)
        MainWindow.setStyleSheet(u"#topBarWidget{\n"
"	background-color: #504c4f;\n"
"	/*background-color: #665c70*/\n"
"}\n"
"\n"
"QFrame{\n"
"	border: none;\n"
"}\n"
"\n"
"#screenWidget{\n"
"	background-color: #302d33\n"
"}\n"
"\n"
"#copyBtn, #cutBtn, #prevBtn, #nextBtn{\n"
"	border:none\n"
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
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

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
        self.verticalLayout_2 = QVBoxLayout(self.screenWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topBarWidget = QWidget(self.screenWidget)
        self.topBarWidget.setObjectName(u"topBarWidget")
        self.horizontalLayout_7 = QHBoxLayout(self.topBarWidget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 10, 0)
        self.frame_4 = QFrame(self.topBarWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.copyBtn = QPushButton(self.frame_4)
        self.copyBtn.setObjectName(u"copyBtn")
        self.copyBtn.setMaximumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(u":/icons/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.copyBtn.setIcon(icon2)
        self.copyBtn.setIconSize(QSize(35, 35))

        self.horizontalLayout_6.addWidget(self.copyBtn)

        self.prevBtn = QPushButton(self.frame_4)
        self.prevBtn.setObjectName(u"prevBtn")
        self.prevBtn.setMaximumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u":/icons/left arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prevBtn.setIcon(icon3)
        self.prevBtn.setIconSize(QSize(35, 35))

        self.horizontalLayout_6.addWidget(self.prevBtn)

        self.nextBtn = QPushButton(self.frame_4)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setMinimumSize(QSize(25, 25))
        self.nextBtn.setMaximumSize(QSize(50, 50))
        icon4 = QIcon()
        icon4.addFile(u":/icons/right arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextBtn.setIcon(icon4)
        self.nextBtn.setIconSize(QSize(35, 35))

        self.horizontalLayout_6.addWidget(self.nextBtn)

        self.cutBtn = QPushButton(self.frame_4)
        self.cutBtn.setObjectName(u"cutBtn")
        self.cutBtn.setMaximumSize(QSize(50, 50))
        icon5 = QIcon()
        icon5.addFile(u":/icons/cut.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cutBtn.setIcon(icon5)
        self.cutBtn.setIconSize(QSize(35, 35))

        self.horizontalLayout_6.addWidget(self.cutBtn)


        self.horizontalLayout_7.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.saveBtn = QPushButton(self.topBarWidget)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_7.addWidget(self.saveBtn)


        self.verticalLayout_2.addWidget(self.topBarWidget)

        self.widget_2 = QWidget(self.screenWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 9)
        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(50, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_5)

        self.textEdit = QTextEdit(self.widget_2)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_5.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.screenWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VorText Text Editor", None))
        self.logo.setText("")
        self.reduceBtn.setText("")
        self.resizeBtn.setText("")
        self.quitBtn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.copyBtn.setText("")
        self.prevBtn.setText("")
        self.nextBtn.setText("")
        self.cutBtn.setText("")
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.saveBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

