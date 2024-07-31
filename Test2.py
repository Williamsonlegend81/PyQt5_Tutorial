from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton
from PyQt5 import uic
import time

t1 = time.time()
class SecondUI(QMainWindow):
    def __init__(self,main_w):
        super(SecondUI,self).__init__()

        # Load the UI file
        uic.loadUi("sample2.ui",self)

        # Load the Widgets
        self.closewin = self.findChild(QPushButton,"pushButton")

        self.closewin.clicked.connect(lambda: self.close_win(main_w))

        self.show()
    
    def close_win(self,main_w):
        t2 = time.time()-t1
        main_w.label1.setText(f"Time in which window 2 was opened is {t2:.2f} seconds")
        self.close()
