from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("image_viewer_2.ui", self)

        # Add Widgets to the App
        self.mylabel = self.findChild(QLabel, "label")
        self.forward = self.findChild(QPushButton, "pushButton_2")
        self.backward = self.findChild(QPushButton, "pushButton")

        self.myImg1 = "E:\\Tkinter Tutorial\\Pokemon\\Legendary\\384_Rayquaza.jpg"
        self.myImg2 = "E:\\Tkinter Tutorial\\Pokemon\\Legendary\\483_Dialga.jpg"
        self.myImg3 = "E:\\Tkinter Tutorial\\Pokemon\\Legendary\\484_Palkia.jpg"
        self.myImg4 = "E:\\Tkinter Tutorial\\Pokemon\\Legendary\\487_Giratina.jpg"
        self.myImg5 = "E:\\Tkinter Tutorial\\Pokemon\\Legendary\\493_Arceus.jpg"
        self.my_list = [self.myImg1,self.myImg2,self.myImg3,self.myImg4,self.myImg5]

        self.image_number = 1
        
        self.backward.setEnabled(False)
        self.forward.clicked.connect(lambda: self.move_forward(2, self.my_list))
        # self.pixmap = QPixmap(my_list[self.number-1][0])
        # self.mylabel.setPixmap(self.pixmap)

        # Show the App
        self.show()
    
    def move_forward(self, number, lister):
        self.backward.setEnabled(True)
        self.forward.setEnabled(True)
        self.pixmap = QPixmap(lister[number-1])
        self.mylabel.setPixmap(self.pixmap)

        if (number==5):
            self.forward.setEnabled(False)
        self.forward.clicked.connect(lambda: self.move_forward(number+1, lister))
        self.backward.clicked.connect(lambda: self.move_backward(number-1, lister))
    def move_backward(self, number, lister):
        self.backward.setEnabled(True)
        self.forward.setEnabled(True)
        self.pixmap = QPixmap(lister[number-1])
        self.mylabel.setPixmap(self.pixmap)

        if (number==1):
            self.backward.setEnabled(False)
        self.forward.clicked.connect(lambda: self.move_forward(number+1, lister))
        self.backward.clicked.connect(lambda: self.move_backward(number-1, lister))

app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()