#This is the GUI file which is imported in Certificate Generator.py. This file has been generated from QT Designer

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(931, 781)
        icon = QIcon()
        icon.addFile(u":/Icon/ISA-logo-jpg.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_8 = QFrame(self.tab_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame_8)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(12, 100, 833, 81))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(163, 20, 621, 24))
        font = QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 147, 22))
        font1 = QFont()
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.frame_3 = QFrame(self.frame_8)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(12, 188, 833, 81))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(163, 20, 621, 24))
        self.lineEdit_2.setFont(font)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 147, 22))
        self.label_2.setFont(font1)
        self.frame_4 = QFrame(self.frame_8)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(12, 276, 833, 81))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 147, 22))
        self.label_3.setFont(font1)
        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(163, 10, 621, 24))
        self.lineEdit_3.setFont(font)
        self.frame_5 = QFrame(self.frame_8)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(12, 364, 833, 81))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 147, 22))
        self.label_4.setFont(font1)
        self.lineEdit_4 = QLineEdit(self.frame_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(163, 10, 621, 24))
        self.lineEdit_4.setFont(font)
        self.frame_6 = QFrame(self.frame_8)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(12, 452, 833, 81))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 131, 22))
        self.label_5.setFont(font1)
        self.lineEdit_5 = QLineEdit(self.frame_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(160, 10, 137, 22))
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(12, 540, 833, 81))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 0, 42, 22))
        self.label_6.setFont(font1)
        self.lineEdit_6 = QLineEdit(self.frame_7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(160, 0, 241, 22))
        self.lineEdit_6.setMinimumSize(QSize(100, 0))
        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(370, 50, 93, 28))
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(290, 20, 251, 71))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_7.setFont(font2)

        self.gridLayout_6.addWidget(self.frame_8, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_8 = QLabel(self.tab_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(310, -10, 251, 81))
        self.label_8.setFont(font2)
        self.frame_9 = QFrame(self.tab_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(40, 70, 571, 48))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_7 = QLineEdit(self.frame_9)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font)

        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 1, 1, 1)

        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.tab_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(40, 130, 411, 48))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_10)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_3.addWidget(self.lineEdit_8, 0, 1, 1, 1)

        self.frame_11 = QFrame(self.tab_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(40, 190, 591, 47))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_11 = QLabel(self.frame_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.frame_11)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(241, 22))
        self.lineEdit_9.setMaximumSize(QSize(241, 22))

        self.gridLayout_5.addWidget(self.lineEdit_9, 0, 1, 1, 1)

        self.toolButton = QToolButton(self.frame_11)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout_5.addWidget(self.toolButton, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.label_23 = QLabel(self.frame_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.gridLayout_5.addWidget(self.label_23, 0, 4, 1, 1)

        self.lineEdit_20 = QLineEdit(self.frame_11)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(51, 22))
        self.lineEdit_20.setMaximumSize(QSize(51, 22))

        self.gridLayout_5.addWidget(self.lineEdit_20, 0, 5, 1, 1)

        self.frame_12 = QFrame(self.tab_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(40, 300, 802, 155))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.frame_12)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(251, 131))

        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_13 = QFrame(self.frame_15)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(401, 50))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_13)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.horizontalLayout.addWidget(self.label_15)

        self.lineEdit_12 = QLineEdit(self.frame_13)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(231, 22))
        self.lineEdit_12.setMaximumSize(QSize(231, 22))

        self.horizontalLayout.addWidget(self.lineEdit_12)

        self.toolButton_2 = QToolButton(self.frame_13)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setMaximumSize(QSize(27, 22))

        self.horizontalLayout.addWidget(self.toolButton_2)


        self.verticalLayout.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_15)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(421, 47))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_22)

        self.lineEdit_19 = QLineEdit(self.frame_14)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMinimumSize(QSize(51, 22))
        self.lineEdit_19.setMaximumSize(QSize(51, 22))

        self.horizontalLayout_2.addWidget(self.lineEdit_19)

        self.horizontalSpacer_3 = QSpacerItem(19, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_16)

        self.lineEdit_13 = QLineEdit(self.frame_14)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMaximumSize(QSize(113, 22))

        self.horizontalLayout_2.addWidget(self.lineEdit_13)


        self.verticalLayout.addWidget(self.frame_14)


        self.gridLayout.addWidget(self.frame_15, 0, 2, 1, 1)

        self.frame_16 = QFrame(self.tab_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(40, 450, 839, 47))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_17 = QLabel(self.frame_16)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_17)

        self.lineEdit_18 = QLineEdit(self.frame_16)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(231, 22))
        self.lineEdit_18.setMaximumSize(QSize(231, 22))

        self.horizontalLayout_3.addWidget(self.lineEdit_18)

        self.toolButton_3 = QToolButton(self.frame_16)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_3.addWidget(self.toolButton_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_21 = QLabel(self.frame_16)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_21)

        self.lineEdit_14 = QLineEdit(self.frame_16)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMaximumSize(QSize(51, 22))

        self.horizontalLayout_3.addWidget(self.lineEdit_14)

        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_18 = QLabel(self.frame_16)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_18)

        self.lineEdit_15 = QLineEdit(self.frame_16)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMaximumSize(QSize(113, 22))

        self.horizontalLayout_3.addWidget(self.lineEdit_15)

        self.frame_17 = QFrame(self.tab_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(40, 510, 581, 46))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_17)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_19 = QLabel(self.frame_17)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.gridLayout_8.addWidget(self.label_19, 0, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.frame_17)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMaximumSize(QSize(361, 22))

        self.gridLayout_8.addWidget(self.lineEdit_16, 0, 1, 1, 1)

        self.toolButton_4 = QToolButton(self.frame_17)
        self.toolButton_4.setObjectName(u"toolButton_4")

        self.gridLayout_8.addWidget(self.toolButton_4, 0, 2, 1, 1)

        self.frame_18 = QFrame(self.tab_4)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(40, 560, 571, 46))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_18)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.gridLayout_9.addWidget(self.label_20, 0, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.frame_18)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMaximumSize(QSize(381, 22))

        self.gridLayout_9.addWidget(self.lineEdit_17, 0, 1, 1, 1)

        self.toolButton_5 = QToolButton(self.frame_18)
        self.toolButton_5.setObjectName(u"toolButton_5")

        self.gridLayout_9.addWidget(self.toolButton_5, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.tab_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(380, 610, 93, 28))
        self.pushButton_2.setMaximumSize(QSize(93, 28))
        self.frame_19 = QFrame(self.tab_4)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(40, 250, 487, 46))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_19)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_14 = QLabel(self.frame_19)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.frame_19)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMaximumSize(QSize(113, 22))

        self.gridLayout_4.addWidget(self.lineEdit_11, 0, 1, 1, 1)

        self.label_12 = QLabel(self.frame_19)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout_4.addWidget(self.label_12, 0, 2, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_19)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMaximumSize(QSize(113, 22))
        self.lineEdit_10.setFont(font)

        self.gridLayout_4.addWidget(self.lineEdit_10, 0, 3, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 931, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Certificate Generator", None))
        self.lineEdit.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Spreadsheet_ID 1:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Spreadsheet_ID 2:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Spreadsheet_ID 3:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Spreadsheet_ID 4:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Workshop Code:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Year:", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year in which workshop was conducted", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Unique ID Generator", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Certificate Generator", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Final Spreadsheet ID generated from ID Generator", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Spreadsheet_ID:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Workshop Name:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Name Font:", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Not Set", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Font Size:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Content:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Content Font:", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Not Set", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Font Size:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Content Colour:", None))
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RGB Colour", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"UQID Font:", None))
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Not Set", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Font Size:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"UQID Colour:", None))
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RGB Colour", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Template Location:", None))
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Not Set", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Save Location:", None))
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Not Set", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Name Colour:", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RGB Colours", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Y-Coordinate:", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"For Name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi
