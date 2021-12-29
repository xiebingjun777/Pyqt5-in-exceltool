# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyWindows.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class VBoxLayout(QVBoxLayout):

    def __init__(self, *args):
        super(VBoxLayout, self).__init__(*args)

        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(676, 811)
        MainWindow.setMinimumSize(QtCore.QSize(500, 378))
        MainWindow.setMaximumSize(QtCore.QSize(676, 1000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(50, 40, 481, 261))
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.BaseInfo = QtWidgets.QWidget()
        self.BaseInfo.setObjectName("BaseInfo")
        self.layoutWidget = QtWidgets.QWidget(self.BaseInfo)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 110, 191, 23))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setMinimumSize(QtCore.QSize(0, 0))
        self.label_15.setMaximumSize(QtCore.QSize(63, 65535))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_6.addWidget(self.label_15)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_6.addWidget(self.dateEdit)
        self.layoutWidget1 = QtWidgets.QWidget(self.BaseInfo)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 140, 191, 21))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        self.label_14.setMaximumSize(QtCore.QSize(63, 65535))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.comboBox_9 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_9.setMinimumSize(QtCore.QSize(106, 0))
        self.comboBox_9.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(9)
        self.comboBox_9.setFont(font)
        self.comboBox_9.setEditable(True)
        self.comboBox_9.setIconSize(QtCore.QSize(9, 9))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_9)
        self.horizontalLayout_7.setStretch(1, 1)
        self.widget = QtWidgets.QWidget(self.BaseInfo)
        self.widget.setGeometry(QtCore.QRect(90, 50, 241, 21))
        self.widget.setObjectName("widget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setMaximumSize(QtCore.QSize(65535, 65535))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(170, 0))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(170, 16777215))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_9.addWidget(self.lineEdit_3)
        self.widget1 = QtWidgets.QWidget(self.BaseInfo)
        self.widget1.setGeometry(QtCore.QRect(90, 20, 241, 21))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_21 = QtWidgets.QLabel(self.widget1)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        self.label_21.setMaximumSize(QtCore.QSize(65535, 65535))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_10.addWidget(self.label_21)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(170, 0))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(170, 16777215))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_10.addWidget(self.lineEdit_4)
        self.widget2 = QtWidgets.QWidget(self.BaseInfo)
        self.widget2.setGeometry(QtCore.QRect(90, 80, 211, 21))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.widget2)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.sexlayout = QtWidgets.QHBoxLayout()
        self.sexlayout.setObjectName("sexlayout")
        self.maleButton = QtWidgets.QRadioButton(self.widget2)
        self.maleButton.setObjectName("maleButton")
        self.sexlayout.addWidget(self.maleButton)
        self.femaleButton = QtWidgets.QRadioButton(self.widget2)
        self.femaleButton.setIconSize(QtCore.QSize(20, 20))
        self.femaleButton.setObjectName("femaleButton")
        self.sexlayout.addWidget(self.femaleButton)
        self.horizontalLayout_8.addLayout(self.sexlayout)
        self.horizontalLayout_8.setStretch(1, 3)
        self.widget3 = QtWidgets.QWidget(self.BaseInfo)
        self.widget3.setGeometry(QtCore.QRect(90, 200, 241, 21))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.widget3)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setMaximumSize(QtCore.QSize(65535, 65535))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.comboBox_6 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_6.setMinimumSize(QtCore.QSize(170, 0))
        self.comboBox_6.setMaximumSize(QtCore.QSize(170, 16777215))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_6)
        self.layoutWidget_2 = QtWidgets.QWidget(self.BaseInfo)
        self.layoutWidget_2.setGeometry(QtCore.QRect(90, 170, 191, 21))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        self.label_22.setMaximumSize(QtCore.QSize(65535, 65535))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_12.addWidget(self.label_22)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.layoutWidget_2)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 10, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_12.addWidget(self.dateTimeEdit)
        self.tabWidget.addTab(self.BaseInfo, "")
        self.Polyo = QtWidgets.QWidget()
        self.Polyo.setObjectName("Polyo")
        self.layoutWidget2 = QtWidgets.QWidget(self.Polyo)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 20, 381, 171))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox.setEnabled(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.comboBox_7 = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_7)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.Polyo, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 10, 401, 190))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.comboBox_12 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.horizontalLayout_15.addWidget(self.comboBox_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.comboBox_10 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.horizontalLayout_13.addWidget(self.comboBox_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_16.addWidget(self.label_17)
        self.comboBox_13 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.horizontalLayout_16.addWidget(self.comboBox_13)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_17.addWidget(self.label_18)
        self.comboBox_14 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.horizontalLayout_17.addWidget(self.comboBox_14)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_19.addWidget(self.label_20)
        self.comboBox_16 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.horizontalLayout_19.addWidget(self.comboBox_16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_18.addWidget(self.label_19)
        self.comboBox_15 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.horizontalLayout_18.addWidget(self.comboBox_15)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        self.tabWidget.addTab(self.tab, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 60, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 310, 441, 391))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 310, 151, 391))

        self.frame = QFrame()

        self.listWidget.setObjectName("listWidget")
        with open('QSS/navigator.qss', 'r') as f:
            style = f.read()
            self.setStyleSheet(style)
            # self.frame.setStyleSheet(style)
        self.setLabels()
        self.setListViews()
        self.setLayouts()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_15.setText(_translate("MainWindow", "出生日期："))
        self.label_14.setText(_translate("MainWindow", "年 齡 ：   "))
        self.comboBox_9.setCurrentText(_translate("MainWindow", "0"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_9.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_9.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_9.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_9.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_9.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_9.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_9.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_9.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_9.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_9.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_9.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_9.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_9.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_9.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_9.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_9.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_9.setItemText(20, _translate("MainWindow", "20"))
        self.label_12.setText(_translate("MainWindow", "姓 名 ："))
        self.label_21.setText(_translate("MainWindow", "  ID  ： "))
        self.label_13.setText(_translate("MainWindow", "性 别 ：    "))
        self.maleButton.setText(_translate("MainWindow", "男"))
        self.femaleButton.setText(_translate("MainWindow", "女"))
        self.label_7.setText(_translate("MainWindow", "肠镜诊断："))
        self.comboBox_6.setCurrentText(_translate("MainWindow", "正常"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "正常"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "息肉"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "癌"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "其他"))
        self.label_22.setText(_translate("MainWindow", "检查时间："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BaseInfo), _translate("MainWindow", "基本信息"))
        self.label.setText(_translate("MainWindow", "息肉部位："))
        self.comboBox.setCurrentText(_translate("MainWindow", "右半结肠（包括：回盲部、升结肠、横结肠右半）"))
        self.comboBox.setItemText(0, _translate("MainWindow", "右半结肠（包括：回盲部、升结肠、横结肠右半）"))
        self.comboBox.setItemText(1, _translate("MainWindow", "左半结肠（包括：横结肠左半、降结肠、乙状结肠）"))
        self.comboBox.setItemText(2, _translate("MainWindow", "直肠"))
        self.comboBox.setItemText(3, _translate("MainWindow", "全大肠散发"))
        self.label_2.setText(_translate("MainWindow", "内镜表现："))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "有蒂"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "有蒂"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "亚蒂"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "平坦"))
        self.label_3.setText(_translate("MainWindow", "息肉病理诊断："))
        self.comboBox_3.setCurrentText(_translate("MainWindow", "炎性息肉"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "炎性息肉"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "增生性息肉"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "腺癌息肉"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "不典型增生/癌变"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "癌"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "锯齿状腺瘤"))
        self.label_4.setText(_translate("MainWindow", "息肉个数："))
        self.comboBox_4.setCurrentText(_translate("MainWindow", "单个"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "单个"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "多个"))
        self.label_8.setText(_translate("MainWindow", "息肉大小："))
        self.comboBox_7.setCurrentText(_translate("MainWindow", "<5mm"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "<5mm"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "6~9mm"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "10~19mm"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", ">20mm"))
        self.comboBox_7.setItemText(4, _translate("MainWindow", ">40mm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Polyo), _translate("MainWindow", "息肉"))
        self.label_16.setText(_translate("MainWindow", "癌灶个数："))
        self.comboBox_12.setCurrentText(_translate("MainWindow", "请选择"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "请选择"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "单个"))
        self.comboBox_12.setItemText(2, _translate("MainWindow", "多个"))
        self.label_10.setText(_translate("MainWindow", "内镜形态："))
        self.comboBox_10.setCurrentText(_translate("MainWindow", "请选择"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "请选择"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "肿块型"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "溃疡型"))
        self.comboBox_10.setItemText(3, _translate("MainWindow", "浸润型"))
        self.label_17.setText(_translate("MainWindow", "病理按分化程度："))
        self.comboBox_13.setCurrentText(_translate("MainWindow", "请选择"))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "请选择"))
        self.comboBox_13.setItemText(1, _translate("MainWindow", "高分化"))
        self.comboBox_13.setItemText(2, _translate("MainWindow", "中分化"))
        self.comboBox_13.setItemText(3, _translate("MainWindow", "低分化"))
        self.comboBox_13.setItemText(4, _translate("MainWindow", "未分化"))
        self.label_18.setText(_translate("MainWindow", "病理按形态分类："))
        self.comboBox_14.setCurrentText(_translate("MainWindow", "请选择"))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "请选择"))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "乳头状"))
        self.comboBox_14.setItemText(2, _translate("MainWindow", "管状"))
        self.comboBox_14.setItemText(3, _translate("MainWindow", "印戎细胞"))
        self.comboBox_14.setItemText(4, _translate("MainWindow", "粘液癌"))
        self.label_20.setText(_translate("MainWindow", "病理按组织来源："))
        self.comboBox_16.setCurrentText(_translate("MainWindow", "请选择"))
        self.comboBox_16.setItemText(0, _translate("MainWindow", "请选择"))
        self.comboBox_16.setItemText(1, _translate("MainWindow", "腺癌"))
        self.comboBox_16.setItemText(2, _translate("MainWindow", "鳞癌"))
        self.comboBox_16.setItemText(3, _translate("MainWindow", "神经分泌肿瘤"))
        self.label_19.setText(_translate("MainWindow", "部   位："))
        self.comboBox_15.setCurrentText(_translate("MainWindow", "请选择"))
        self.comboBox_15.setItemText(0, _translate("MainWindow", "请选择"))
        self.comboBox_15.setItemText(1, _translate("MainWindow", "左半结肠"))
        self.comboBox_15.setItemText(2, _translate("MainWindow", "右半结肠"))
        self.comboBox_15.setItemText(3, _translate("MainWindow", "直肠"))
        self.comboBox_15.setItemText(4, _translate("MainWindow", "两处以上"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "癌"))
        self.pushButton.setText(_translate("MainWindow", "添加信息"))

    def setLabels(self):
        """定义所有的标签。"""
        self.recommendLabel = QLabel(" 推荐")
        self.recommendLabel.setObjectName("recommendLabel")
        self.recommendLabel.setMaximumHeight(27)

        self.myMusic = QLabel(" 我的音乐")
        self.myMusic.setObjectName("myMusic")
        self.myMusic.setMaximumHeight(27)
        # self.myMusic.setMaximumHeight(54)

        self.singsListLabel = QLabel(" 收藏与创建的歌单")
        self.singsListLabel.setObjectName("singsListLabel")
        self.singsListLabel.setMaximumHeight(27)

    def setListViews(self):
        """定义承载功能的ListView"""
        # self.listWidget = QListWidget()
        self.listWidget.setMaximumHeight(110)
        self.listWidget.setObjectName("navigationList")
        self.listWidget.addItem(QListWidgetItem(QIcon('resources/music.png'), " 发现音乐"))
        self.listWidget.addItem(QListWidgetItem(QIcon('resources/signal.png'), " 私人FM"))
        self.listWidget.addItem(QListWidgetItem(QIcon('resources/movie.png'), " MV"))
        self.listWidget.setCurrentRow(0)



    def setLayouts(self):
        """定义布局。"""
        self.mainLayout = VBoxLayout(self.frame)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addWidget(self.recommendLabel)
        self.mainLayout.addSpacing(3)
        self.mainLayout.addSpacing(1)

        self.mainLayout.addWidget(self.myMusic)
        self.mainLayout.addSpacing(3)
        self.mainLayout.addSpacing(1)

        self.mainLayout.addWidget(self.singsListLabel)
        self.mainLayout.addSpacing(1)

        self.mainLayout.addStretch(1)

        self.setContentsMargins(0, 0, 0, 0)
