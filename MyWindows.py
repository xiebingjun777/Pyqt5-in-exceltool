# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyWindows.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(676, 378)
        MainWindow.setMinimumSize(QtCore.QSize(676, 378))
        MainWindow.setMaximumSize(QtCore.QSize(676, 378))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 481, 261))
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.BaseInfo = QtWidgets.QWidget()
        self.BaseInfo.setObjectName("BaseInfo")
        self.widget = QtWidgets.QWidget(self.BaseInfo)
        self.widget.setGeometry(QtCore.QRect(10, 10, 341, 211))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 43))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_9.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.sexlayout = QtWidgets.QHBoxLayout()
        self.sexlayout.setObjectName("sexlayout")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(120, 43))
        self.label_6.setMaximumSize(QtCore.QSize(100, 43))
        self.label_6.setBaseSize(QtCore.QSize(100, 30))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.sexlayout.addWidget(self.label_6)
        self.maleButton = QtWidgets.QRadioButton(self.widget)
        self.maleButton.setObjectName("maleButton")
        self.sexlayout.addWidget(self.maleButton)
        self.femaleButton = QtWidgets.QRadioButton(self.widget)
        self.femaleButton.setIconSize(QtCore.QSize(20, 20))
        self.femaleButton.setObjectName("femaleButton")
        self.sexlayout.addWidget(self.femaleButton)
        self.horizontalLayout_8.addLayout(self.sexlayout)
        self.horizontalLayout_8.setStretch(1, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.comboBox_9 = QtWidgets.QComboBox(self.widget)
        self.comboBox_9.setMinimumSize(QtCore.QSize(170, 0))
        self.comboBox_9.setMaximumSize(QtCore.QSize(170, 16777215))
        self.comboBox_9.setEditable(True)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_6.addWidget(self.label_15)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_6.addWidget(self.dateEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(160, 0))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.comboBox_6 = QtWidgets.QComboBox(self.widget)
        self.comboBox_6.setMinimumSize(QtCore.QSize(170, 0))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.tabWidget.addTab(self.BaseInfo, "")
        self.Polyo = QtWidgets.QWidget()
        self.Polyo.setObjectName("Polyo")
        self.widget1 = QtWidgets.QWidget(self.Polyo)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 471, 218))
        self.widget1.setObjectName("widget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget1)
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
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget1)
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
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.comboBox_7 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_7)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.tabWidget.addTab(self.Polyo, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget2 = QtWidgets.QWidget(self.tab)
        self.widget2.setGeometry(QtCore.QRect(30, 10, 401, 190))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.widget2)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.comboBox_12 = QtWidgets.QComboBox(self.widget2)
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.horizontalLayout_15.addWidget(self.comboBox_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.widget2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.comboBox_10 = QtWidgets.QComboBox(self.widget2)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.horizontalLayout_13.addWidget(self.comboBox_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_17 = QtWidgets.QLabel(self.widget2)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_16.addWidget(self.label_17)
        self.comboBox_13 = QtWidgets.QComboBox(self.widget2)
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
        self.label_18 = QtWidgets.QLabel(self.widget2)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_17.addWidget(self.label_18)
        self.comboBox_14 = QtWidgets.QComboBox(self.widget2)
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
        self.label_20 = QtWidgets.QLabel(self.widget2)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_19.addWidget(self.label_20)
        self.comboBox_16 = QtWidgets.QComboBox(self.widget2)
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.horizontalLayout_19.addWidget(self.comboBox_16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_19 = QtWidgets.QLabel(self.widget2)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_18.addWidget(self.label_19)
        self.comboBox_15 = QtWidgets.QComboBox(self.widget2)
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
        self.pushButton.setGeometry(QtCore.QRect(520, 60, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_12.setText(_translate("MainWindow", "??? ??? ???"))
        self.label_13.setText(_translate("MainWindow", "??? ??? ???"))
        self.maleButton.setText(_translate("MainWindow", "???"))
        self.femaleButton.setText(_translate("MainWindow", "???"))
        self.label_14.setText(_translate("MainWindow", "???   ??? ???"))
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
        self.label_15.setText(_translate("MainWindow", "???????????????"))
        self.label_7.setText(_translate("MainWindow", "???????????????"))
        self.comboBox_6.setCurrentText(_translate("MainWindow", "??????"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "??????"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "??????"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "???"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "??????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BaseInfo), _translate("MainWindow", "????????????"))
        self.label.setText(_translate("MainWindow", "???????????????"))
        self.comboBox.setCurrentText(_translate("MainWindow", "??????????????????????????????????????????????????????????????????"))
        self.comboBox.setItemText(0, _translate("MainWindow", "??????????????????????????????????????????????????????????????????"))
        self.comboBox.setItemText(1, _translate("MainWindow", "?????????????????????????????????????????????????????????????????????"))
        self.comboBox.setItemText(2, _translate("MainWindow", "??????"))
        self.comboBox.setItemText(3, _translate("MainWindow", "???????????????"))
        self.label_2.setText(_translate("MainWindow", "???????????????"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "??????"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "??????"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "??????"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "??????"))
        self.label_3.setText(_translate("MainWindow", "?????????????????????"))
        self.comboBox_3.setCurrentText(_translate("MainWindow", "????????????"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "????????????"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "???????????????"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "????????????"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "???????????????/??????"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "???"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "???????????????"))
        self.label_4.setText(_translate("MainWindow", "???????????????"))
        self.comboBox_4.setCurrentText(_translate("MainWindow", "??????"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "??????"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "??????"))
        self.label_8.setText(_translate("MainWindow", "???????????????"))
        self.comboBox_7.setCurrentText(_translate("MainWindow", "<5mm"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "<5mm"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "6~9mm"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "10~19mm"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", ">20mm"))
        self.comboBox_7.setItemText(4, _translate("MainWindow", ">40mm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Polyo), _translate("MainWindow", "??????"))
        self.label_16.setText(_translate("MainWindow", "???????????????"))
        self.comboBox_12.setCurrentText(_translate("MainWindow", "?????????"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "?????????"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "??????"))
        self.comboBox_12.setItemText(2, _translate("MainWindow", "??????"))
        self.label_10.setText(_translate("MainWindow", "???????????????"))
        self.comboBox_10.setCurrentText(_translate("MainWindow", "?????????"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "?????????"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "?????????"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "?????????"))
        self.comboBox_10.setItemText(3, _translate("MainWindow", "?????????"))
        self.label_17.setText(_translate("MainWindow", "????????????????????????"))
        self.comboBox_13.setCurrentText(_translate("MainWindow", "?????????"))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "?????????"))
        self.comboBox_13.setItemText(1, _translate("MainWindow", "?????????"))
        self.comboBox_13.setItemText(2, _translate("MainWindow", "?????????"))
        self.comboBox_13.setItemText(3, _translate("MainWindow", "?????????"))
        self.comboBox_13.setItemText(4, _translate("MainWindow", "?????????"))
        self.label_18.setText(_translate("MainWindow", "????????????????????????"))
        self.comboBox_14.setCurrentText(_translate("MainWindow", "?????????"))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "?????????"))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "?????????"))
        self.comboBox_14.setItemText(2, _translate("MainWindow", "??????"))
        self.comboBox_14.setItemText(3, _translate("MainWindow", "????????????"))
        self.comboBox_14.setItemText(4, _translate("MainWindow", "?????????"))
        self.label_20.setText(_translate("MainWindow", "????????????????????????"))
        self.comboBox_16.setCurrentText(_translate("MainWindow", "?????????"))
        self.comboBox_16.setItemText(0, _translate("MainWindow", "?????????"))
        self.comboBox_16.setItemText(1, _translate("MainWindow", "??????"))
        self.comboBox_16.setItemText(2, _translate("MainWindow", "??????"))
        self.comboBox_16.setItemText(3, _translate("MainWindow", "??????????????????"))
        self.label_19.setText(_translate("MainWindow", "???   ??????"))
        self.comboBox_15.setCurrentText(_translate("MainWindow", "?????????"))
        self.comboBox_15.setItemText(0, _translate("MainWindow", "?????????"))
        self.comboBox_15.setItemText(1, _translate("MainWindow", "????????????"))
        self.comboBox_15.setItemText(2, _translate("MainWindow", "????????????"))
        self.comboBox_15.setItemText(3, _translate("MainWindow", "??????"))
        self.comboBox_15.setItemText(4, _translate("MainWindow", "????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "???"))
        self.pushButton.setText(_translate("MainWindow", "????????????"))
