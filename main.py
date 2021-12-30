import datetime
import sys
import time
import os
from MyWindows import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import xlwt
import xlrd
import openpyxl
from xlutils.copy import copy
from xlsxwriter import Workbook

add_count = 1
ouput_excel = "patient_info_temp.xlsx"
# workbook = xlrd.open_workbook(ouput_excel)
# workbook =
# worksheet = workbook.add_sheet('sheet1')
# rows = workbook.sheets()[0].nrows
# worksheet.write(0, 0, label='病人ID号')
# worksheet.write(0, 1, label='姓名')
# worksheet.write(0, 2, label='性别')
# worksheet.write(0, 3, label='年龄')
# worksheet.write(0, 4, label='出生日期')
# worksheet.write(0, 5, label='检查日期')
# worksheet.write(0, 6, label='诊断')
# worksheet.write(0, 7, label='其他')
# worksheet.write(0, 8, label='息肉个数')
# worksheet.write(0, 9, label='息肉部位')
# worksheet.write(0, 10, label='内镜表现')
# worksheet.write(0, 11, label='息肉病理诊断')
# worksheet.write(0, 12, label='癌灶个数')
# worksheet.write(0, 13, label='病理：按分化程度')
# worksheet.write(0, 14, label='病理：按形态分类')
# worksheet.write(0, 15, label='内镜形态')
# worksheet.write(0, 16, label='病理：按组织来源')
# worksheet.write(0, 17, label='部位')
patient_title = ['病人ID号','姓名','性别','年龄','出生日期','检查日期','诊断','其他','息肉个数','息肉大小','息肉部位','内镜表现','息肉病理诊断','癌灶个数','病理：按分化程度','病理：按形态分类','内镜形态','病理：按组织来源','部位']
patient_key = ["ID","Name","Sex","Age","BirthDay","CheckDate","Diagnose","OtherDia","PolyoCount",
               "PolyoSize","PolyoSite","Endoscope","PolyoPathology","CancerFociCount","DifferePathology",
               "ShapePathology","EndoscopeShape","HistologicPathology","CancerSite"]
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
# print(len(patient_info.keys()))
print(patient_info.keys())


def writeExcel(path,dic_info,count=1):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "sheet1"
    k_list = []
    v_list = []
    for key, value in dic_info.items():
        k_list.append(key)
        v_list.append(value)
        for i in range(0,len(k_list)):
            sheet.cell(row=1,column=i+1,value=k_list[i])
            for j in range(0,len(v_list)):
                sheet.cell(row=i+2,column=j+1,value=v_list[j])
    workbook.save(path)

def writeExcelAppend(path,dic_info,count=1):
    workbook = xlrd.open_workbook(path)
    sheet_name = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheet_name[0])
    rows_exist = worksheet.nrows
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)
    v_list = []
    for key, value in dic_info.items():
        v_list.append(value)
        for j in range(0,len(v_list)):
            new_worksheet.write(rows_exist,j,v_list[j])
    new_workbook.save(path)

class myWin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(myWin,self).__init__()
        self.setupUi(self)
        self.initWidgetsParm()
        self.tabItem = {"癌":self.tab,"息肉":self.Polyo,"正常":"","其他":""}
        self.tabItemList = [{"正常": "","checkResult" : 0},{"息肉": self.Polyo,"checkResult" : 1},{"癌": self.tab,"checkResult" : 2},{"其他":"","checkResult" : 3}]
        self.isCheck = False
        self.addCount = 1
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
            self.setStyleSheet("QLineEdit#lineEdit_4 { border:1px solid #FF5959;background-color:#E4F0FA}")
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
        self.addCount += 1

        if not os.path.exists(ouput_excel):
            file = open(ouput_excel, 'w')
            file.close()
            # wb = Workbook(ouput_excel)
            # sh1 = wb.add_worksheet("sheet1")
            # wb = Workbook(ouput_excel)
            # sh1 = wb.add_worksheet("sheet1")
            # wb.save(ouput_excel)
        workbook = xlrd.open_workbook(ouput_excel)
        sheet_name = workbook.sheet_names()
        worksheet = workbook.sheet_by_name(sheet_name[0])
        rows_exists = worksheet.nrows

        if rows_exists == 0 :
            writeExcel(ouput_excel,patient_info)
        else:
            writeExcelAppend(ouput_excel,patient_info)

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
        if self.isCheck or tabTitle == "正常" or tabTitle == "" or tabTitle == "其他":
            return
        self.tabWidget.addTab(self.tabItem[tabTitle], tabTitle)
        self.isCheck = True
        self.tabWidget.setCurrentIndex(1)

    def closeTab(self,item):
        print(item)
        if self.tabWidget.count() == 1:
            return
        self.tabWidget.removeTab(item)
        self.isCheck = False
        self.comboBox_6.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = myWin()
    Win.show()
    sys.exit(app.exec_())