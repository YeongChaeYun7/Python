import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import cv2

ui_path = r"Photoshop.ui"
form_class = uic.loadUiType(ui_path)[0]


class WindowClass(QMainWindow, form_class):  # QMainWindow, form_class클래스로부터 다중 상속
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # setupUi 메서드(고정된 이름) 호출로 QtDesigner로 만든 UI 파일 로드
        # UI파일을 코드로 변환하지 않은 이유는 QtDesigner를 통해 수정 반영되게 하려고. 코드 변경 최소화 위해


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
