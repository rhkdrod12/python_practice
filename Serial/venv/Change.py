import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("Serialchanger.ui")[0]

class MyWindow(QDialog, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.Yearchanged)
        self.lineEdit_2.textChanged.connect(self.Qtychanged)
        self.lineEdit_3.textChanged.connect(self.Monthchanged)
        self.lineEdit_4.textChanged.connect(self.Namechanged)

        self.lineEdit.setFocus()

        self.Year = ['J','A','B','C','D','E','F','G','H','I']
        self.Month = ['L', 'A', 'S', 'E', 'R', 'O', 'P', 'T', '2', 'K', 'N', 'D']

        self.Year_Changed_Value = ""
        self.Month_Changed_Value = ""
        self.Qty_Value = ""
        self.Name_Changed_Value =""

    def Yearchanged(self):
        self.Year_Value = list(self.lineEdit.text())

        if len(self.Year_Value) == 4:
            self.Year_Changed_Value = self.Year_Value[2] + self.Year[int(self.Year_Value[3])]
        elif len(self.Year_Value) == 3:
            self.Year_Changed_Value = self.Year_Value[2]
        elif len(self.Year_Value) <= 2:
            self.Year_Changed_Value = ""

        self.text_browser.setText(self.Year_Changed_Value+self.Qty_Value+self.Month_Changed_Value)

    def Qtychanged(self):
        self.Qty_Value=self.lineEdit_2.text()
        self.text_browser.setText(self.Year_Changed_Value+self.Qty_Value+self.Month_Changed_Value)

    def Monthchanged(self):
        if self.lineEdit_3.text():
            self.Month_Value =int(self.lineEdit_3.text())
            if 0 < self.Month_Value <= 12:
                self.Month_Changed_Value = self.Month[self.Month_Value-1]
            else:
                self.Month_Changed_Value = ""
        else:
            self.Month_Changed_Value = ""
        self.text_browser.setText(self.Year_Changed_Value + self.Qty_Value + self.Month_Changed_Value)

    def Namechanged(self):

        if self.lineEdit_4.text():
            self.Name_Value = list(self.lineEdit_4.text())
            print(self.Name_Value)
            Temp=""
            print("확인")
            for Name in self.Name_Value:
                print("Name: "+Name)
                print(type(Name))
                print(type(ord(Name)))
                Temp = Temp + str(ord(Name))
                print("Temp: "+Temp)
            self.Name_Changed_Value = Temp
        else:
            self.Name_Changed_Value=""
        if len(self.Name_Changed_Value) == 4:
            self.Name_Changed_Value = self.Name_Changed_Value + '0'
        self.text_browser.setText(self.Year_Changed_Value + self.Qty_Value + self.Month_Changed_Value+self.Name_Changed_Value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

