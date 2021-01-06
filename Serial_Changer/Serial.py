import sys

from value_change import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("Serialchanger.ui")[0]

class MyWindow(QDialog, form_class):

    def __init__(self):
        super().__init__()
        # 변환데이터
        self.Year = ['J', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.Month = ['','L', 'A', 'S', 'E', 'R', 'O', 'P', 'T', '2', 'K', 'N', 'D']
        self.Name = list(range(48, 123))

        # 변수초기화
        self.Year_Changed_Value = ""
        self.Month_Changed_Value = ""
        self.Qty_Value = ""
        self.Name_Changed_Value = ""

        # ui 선언
        self.setupUi(self)

        # UI 연결 부분
        self.lineEdit.textChanged.connect(self.textChanged)
        self.lineEdit_2.textChanged.connect(self.textChanged)
        self.lineEdit_3.textChanged.connect(self.textChanged)
        self.lineEdit_4.textChanged.connect(self.textChanged)

        # 포커스 지정
        self.lineEdit.setFocus()

    def textChanged(self):
        # 변환부분
        self.Yearchanged()
        self.Qtychanged()
        self.Monthchanged()
        self.Namechanged()
        # 상태 표기
        self.print_state()
        # UI값 표기
        self.text_browser.setText(self.Year_Changed_Value + self.Qty_Value + self.Month_Changed_Value + self.Name_Changed_Value)

    def Yearchanged(self):
        # Val_change(문자열, 글자수 , 변환시작지점, 변환종료지점(맨 끝은 포함하지 않음)
        # 두개만 표기하며 맨 마지막 글자만 변환
        self.Year_Changed_Value = Val_change((self.lineEdit.text())[2:], self.Year, 1, 1, 2)

    def Qtychanged(self):
        # 있는 그대로 표기
        self.Qty_Value= self.lineEdit_2.text()

    def Monthchanged(self):
        # 1~12까지 이므로 두자리까지 변환값으로 인식
        self.Month_Changed_Value = Val_change(self.lineEdit_3.text(), self.Month, 2)

    def Namechanged(self):
        # 영문이니셜 두글자 입력되며 이를 각각 변환
        self.Name_Changed_Value = Val_change(Str_Int(self.lineEdit_4.text()), self.Name, 1)

    def print_state(self):
        # 상태 표기용
        print("Year  : ", self.Year_Changed_Value)
        print("Qty   : ", self.Qty_Value)
        print("Month : ", self.Month_Changed_Value)
        print("Name  : ", self.Name_Changed_Value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()