import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

ui_path = r"PYQTPaintbrush.ui"  # 파일명과 동일해야 로드 가능
form_class = uic.loadUiType("ui_path")[0]  # ui_path파일을 로드해서 만든 클래스


class WindowClass(QMainWindow, form_class):  # QMainWindow, form_class클래스로부터 다중 상속
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # setupUi 메서드 호출로 QtDesigner로 만든 UI 파일 로드
        # UI파일을 코드로 변환하지 않은 이유는 QtDesigner를 통해 ㅅㅜㅣㅂㄱㅔ 수정 반영되게 하려고. 코드 변경 최소화 위해

        self.brushColor = Qt.black  # brushColor 기본 값

        # id.canvas(Label)을 cavas형식으로 변경
        self.canvas = QtGui.QPixmap(  # QPixmap객체 추가. QPixmap이 가져오는 이미지를 Label에 표시
            self.lb_canvas.width(), self.lb_canvas.height())
        self.canvas.fill(QtGui.QColor("white"))
        # setPixmap(): PyQt에서 이미지를 보여줄 때 사용
        self.lb_canvas.setPixmap(self.canvas)

        # 각각의 버튼 색(기능) 정의
        self.btn_black.clicked.connect(self.btn_clicked)
        self.btn_black.setStyleSheet('background:black')

        self.btn_red.clicked.connect(self.btn_clicked)
        self.btn_red.setStyleSheet('background:red')

        self.btn_blue.clicked.connect(self.btn_clicked)
        self.btn_blue.setStyleSheet('background:blue')

    # btn_ 버튼 클릭 시 실행. 버튼에 따라 브러쉬 색상 결정
    def btn_clicked(self):
        btn_value = self.sender().objectName()
        print(btn_value)
        if btn_value == 'btn_black':
            self.brushColor = Qt.black
        elif btn_value == 'btn_red':
            self.brushColor = Qt.red
        elif btn_value == 'btn_blue':
            self.brushColor = Qt.blue

    # btn_clear 버튼 클릭 시 실행
    def bte_clear_clicked(self):
        print('모두 지움')
        self.canvas.fill(QtGui.QColor("white"))  # white로 canvas채움 -> 지워진것같은 효과
        self.lb_canvas.setPixmap(self.canvas)

    # 큐티디자이너 캔버스에 마우스좌표 반환 체크함
    def mouseMoveEvent(self, e):  # 마우스의 현재 위치 반환
        painter = QtGui.QPainter(self.lb_canvas.pixmap())
        painter.setPen(QPen(self.brushColor, 5, Qt.SolidLine, Qt.RoundCap))
        painter.drawPoint(e.x(), e.y())
        painter.end()
        self.update()
        #print(e.x(), e.y())

    # def brushSize(self):
    #     btn_value = self.sender().objectName()
    #     if btn_value == 'btn_black':
    #         self.brushColor = Qt.black
    #     elif btn_value == 'btn_red':
    #         self.brushColor = Qt.red
    #     elif btn_value == 'btn_blue':
    #         self.brushColor = Qt.blue


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
