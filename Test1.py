from PyQt5.QtWidgets import QMainWindow,QPushButton,QLabel,QApplication
from PyQt5 import uic
import sys
from Test2 import SecondUI
import time

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        # Load the ui file
        uic.loadUi("sample1.ui",self)

        # Load the Widgets
        self.label1 = self.findChild(QLabel,"label")
        self.button1 = self.findChild(QPushButton,"pushButton")

        self.button1.clicked.connect(self.open_window)

        self.show()
    
    def open_window(self):
        self.window = SecondUI(UIWindow)
        self.window.show()

app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()