import sys
import time
from MyWindows import Ui_MainWindow
from PyQt5.QtWidgets import *
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
        # self.retranslateUi(self)
        # PushSend = self.pushButton
        # qss = '''QPushButton{background-color:red;}'''
        # self.setStyleSheet(qss)
        #
        # PushSend.clicked.connect(self.sendPush)
        #根据出生年月设置来算年龄
        self.dateEdit.dateChanged.connect(self.calAge)

    def sendPush(self):
        print("SendPush has been on clicked")
        print(self.comboBox.currentText())
        print(self.comboBox_2.currentText())

    def calAge(self):
        print("计算年龄")
        print(str(self.dateEdit.date().year()) + "-" + str(self.dateEdit.date().month()) + "-" + str(self.dateEdit.date().day()))
        if self.dateEdit.date().year() < time.localtime(time.time()).tm_year :
            age = time.localtime(time.time()).tm_year - self.dateEdit.date().year()
        else:
            return
        self.comboBox_9.setCurrentText(str(age))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = myWin()
    Win.show()
    sys.exit(app.exec_())