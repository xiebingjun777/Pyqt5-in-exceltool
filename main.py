import datetime
import sys
import time
from MyWindows import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
patient_info = {"ID":0,
                "Name":"",
                "Sex":"",
                "Age":0,
                "BirthDay":"",
                "CheckDate":"",
                "Diagnose":"",
                "OtherDia":"",
                "PolyoCount":0,
                "PolyoSize":"",
                "PolyoSite":"",
                "Endoscope":"",
                "PolyoPathology":"",
                "CancerFociCount":0,
                "DifferePathology":"",
                "ShapePathology":"",
                "EndoscopeShape":"",
                "HistologicPathology":"",
                "CancerSite":""
                }
print(len(patient_info.keys()))
print(patient_info.keys())
class myWin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(myWin,self).__init__()
        self.setupUi(self)
        self.initWidgetsParm()
        self.tabItem = {"癌":self.tab,"息肉":self.Polyo,"正常":"","其他":""}
        self.tabItemList = [{"正常": "","checkResult" : 0},{"息肉": self.Polyo,"checkResult" : 1},{"癌": self.tab,"checkResult" : 2},{"其他":"","checkResult" : 3}]
        self.isCheck = False
        # self.Sex = ["男","女"]
        # self.isCancer = False
        # self.isPolyo = False


        # self.retranslateUi(self)
        # PushSend = self.pushButton
        # qss = '''QPushButton{background-color:red;}'''
        # self.setStyleSheet(qss)
        #
        # self.setStyleSheet("QLineEdit#input { border:1px solid #0F0F0E;} QLineEdit#inputNull { border:1px solid #FF5959;}")
        self.pushButton.clicked.connect(self.sendPush)
        #根据出生年月设置来算年龄
        self.comboBox_6.currentTextChanged.connect(self.addTabItem)
        self.dateEdit.dateChanged.connect(self.calAge)
        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.tabWidget.installEventFilter(self)
        # self.lineEdit_4.

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter :
            print("mouse Enter ")
            self.setStyleSheet("QLineEdit#lineEdit_4,#lineEdit_3 { border:1px solid #828790;}")
            return True
        return False

    def sendPush(self):
        print("SendPush has been on clicked")
        # print(self.comboBox.currentText())
        # print(self.comboBox_2.currentText())
        if self.lineEdit_4.text() == "":
            print("lineEdit_4空")
            self.setStyleSheet("QLineEdit#lineEdit_4 { border:1px solid #FF5959;}")
            return

        if self.lineEdit_3.text() == "":
            print("lineEdit_3空")
            self.setStyleSheet("QLineEdit#lineEdit_3 { border:1px solid #FF5959;}")
            return
        patient_info["ID"] = self.lineEdit_4.text()
        patient_info["Name"] = self.lineEdit_3.text()
        patient_info["Age"] = self.comboBox_9.currentText()
        if self.femaleButton.isChecked():
            patient_info["Sex"] = "女"
        elif self.maleButton.isChecked():
            patient_info["Sex"] = "男"
        patient_info["BirthDay"] = self.dateEdit.date().toString()
        patient_info["CheckDate"] = self.dateTimeEdit.date().toString()
        patient_info["Diagnose"] = self.comboBox_6.currentText()

        print(patient_info)


    def checkCancerInput(self):
        print("check Cancer Input")

    def checkPoyloInput(self):
        print("checkPoyloInput")
    # def changeLineEditBorder(self):
    #     self.lineEdit_4.setStyleSheet("QLineEdit { border:1px solid #0F0F0E;}")

    def calAge(self):
        print("计算年龄")
        print(str(self.dateEdit.date().year()) + "-" + str(self.dateEdit.date().month()) + "-" + str(self.dateEdit.date().day()))
        if self.dateEdit.date().year() < time.localtime(time.time()).tm_year :
            age = time.localtime(time.time()).tm_year - self.dateEdit.date().year()
        else:
            return
        self.comboBox_9.setCurrentText(str(age))

    def initWidgetsParm(self):
        self.dateEdit.setMaximumDate(QDate.currentDate())
        self.dateTimeEdit.setMaximumDate(QDate.currentDate())
        while(self.tabWidget.count() != 1):
            self.tabWidget.removeTab(1)
            self.tabWidget.removeTab(1)

    def addTabItem(self,tabTitle):
        print(tabTitle)
        if self.isCheck or tabTitle == "正常":
            return
        self.tabWidget.addTab(self.tabItem[tabTitle], tabTitle)
        self.isCheck = True

    def closeTab(self,item):
        print(item)
        if self.tabWidget.count() == 1:
            return
        self.tabWidget.removeTab(item)
        self.isCheck = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = myWin()
    Win.show()
    sys.exit(app.exec_())