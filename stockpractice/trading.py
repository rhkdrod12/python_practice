import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *
from PyQt5 import uic

form_class = uic.loadUiType("stock.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.DB=list()


        print("단계: UI연결 ")

        self.setupUi(self)

        self.code_edit.setText("039490")

        self.btn1.clicked.connect(self.btn1_clicked)
        self.btn2.clicked.connect(self.btn2_clicked)

        print("단계: UI연결 완료")

        print("단계: 로그인 시도")

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")        #QAxWidget(키움증권에서 제공하는 클래스를 파이썬에서 사용할 수 있도록 함) kiwoom이름의 인스턴스 생성
        self.kiwoom.dynamicCall("CommConnect()")

        print("단계: 로그인 완료")

        #COM은 마이크로소프트가 만든 컴포넌트 모델(COM은 어떤 컴파일러에서도 그 파일을 사용할 수 있도록 하는 규약)
        #"KHOPENAPI.KHOpenAPICtrl.1"는 Kioom openAPI 컴포넌트의 클래스 ID(CLSID)의 사람이 쉽게 이해하기 쉽도록 만든 ProgID를 의미
        #dynamicCall(QAxWidget의 부포클래스인 QaxBase의 클래스의 메서드)을 사용하여 CommConnect()를 서버로 보냄냄
        #dynamicCall는 COM 객체의 메소드 함수를 호출하여 매개 변수를 전달, 즉 kioom의 객체에 dynamicCall( ) ()안의 값을 보냄
        #위에서는 kioom이라는 COM객체에 CommConnect()을 보냄
        #그리고 키움openAPI에서 CommConnect()는 로그인 명령어로서 로그인 화면을 호출함
        #"KHOPENAPI.KHOpenAPICtrl.1"의 ProgID이름의 컴포넌트를  QAxWidget을 통해 kioom 이라는 이름으로 인스터스를 생성하고 dynamicCall을 사용하여 COM객체 kioom에 CommConnect()명령어를 보냄냄

        print("단계: 이벤트 연결")
        self.kiwoom.OnEventConnect.connect(self.login_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trData)
        self.kiwoom.OnReceiveChejanData.connect(self.receive_ChejanData)
        print("단계: 이벤트 완료")

    def login_connect(self, err_code):
        print("단계: 로그인 시도")

        if err_code == 0:
            self.statusbar.showMessage("로그인 성공")
        elif err_code == 100:
            self.statusbar.showMessage("사용자 정보교환 실패")
        elif err_code == 101:
            self.statusbar.showMessage("서버접속 실패")
        elif err_code == 102:
            self.statusbar.showMessage("버전처리 실패")
        print("단계: 로그인 완료")

    def receive_trData(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        print("단계: TR수신 ")
        print("trcode: ",trcode,"rqname: ", rqname, "recordname: ",recordname)
        if rqname == "opt10001_req":
            self.STDB = {'종목명': '', '거래량': '', '현재가': '', 'PER': '', 'PBR': '', 'ROE': ''}
            for name in self.STDB:
                self.STDB[name]=self.kiwoom.dynamicCall("GetCommData(QString, QString,  int, QString)", trcode, recordname, 0,name).strip()
                if name == "현재가":
                    self.STDB[name] = str(abs(int(self.STDB[name])))

            # self.DB.append(self.STDB)
            print(self.STDB)

            # price=price.strip()
            # print(price)
            # price = int(price)
            # print(type(price))
            # print(price)
            # price = abs(price)
            #
            # self.text_edit.append("종목명 : " + name.strip())
            # self.text_edit.append("거래량 : " + volume.strip())
            # self.text_edit.append("현재가 : " + str(price))
            # self.text_edit.append("PBR    : " + PER.strip())

        print("단계: TR수신 완료 ")

    def receive_ChejanData(self, gubun , itemcnt, fidlist):
        print(" ")

    def btn1_clicked(self):
        print("단계: 기본정보 조회")
        code = self.code_edit.text()

        # SetInputValue
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)
        # CommRqData
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")
        print("단계: 기본정보 조회 완료")


    def btn2_clicked(self):
        print("단계: 계좌번호 얻기")
        account_num = self.kiwoom.dynamicCall("GetLoginInfo(QString)", ["ACCNO"])
        account_num = account_num.rstrip(';')
        self.My_Acc.setText(account_num)
        print("단계: 계좌번호 완료")




if __name__ == "__main__":
    # sys.argv는 현재 py파일이 있는 경로
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()