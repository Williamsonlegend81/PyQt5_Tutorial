from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("tic_tac_toe.ui", self)

        # Define a counter whose turn it is
        self.counter = 0

        # Add the Widgets
        self.btn1 = self.findChild(QPushButton, "pushButton_1")
        self.btn2 = self.findChild(QPushButton, "pushButton_2")
        self.btn3 = self.findChild(QPushButton, "pushButton_3")
        self.btn4 = self.findChild(QPushButton, "pushButton_4")
        self.btn5 = self.findChild(QPushButton, "pushButton_5")
        self.btn6 = self.findChild(QPushButton, "pushButton_6")
        self.btn7 = self.findChild(QPushButton, "pushButton_7")
        self.btn8 = self.findChild(QPushButton, "pushButton_8")
        self.btn9 = self.findChild(QPushButton, "pushButton_9")
        self.btn10 = self.findChild(QPushButton, "pushButton_10")
        self.mylabel = self.findChild(QLabel, "label")
        
        # Click The Button
        self.btn1.clicked.connect(lambda: self.clicker(self.btn1))
        self.btn2.clicked.connect(lambda: self.clicker(self.btn2))
        self.btn3.clicked.connect(lambda: self.clicker(self.btn3))
        self.btn4.clicked.connect(lambda: self.clicker(self.btn4))
        self.btn5.clicked.connect(lambda: self.clicker(self.btn5))
        self.btn6.clicked.connect(lambda: self.clicker(self.btn6))
        self.btn7.clicked.connect(lambda: self.clicker(self.btn7))
        self.btn8.clicked.connect(lambda: self.clicker(self.btn8))
        self.btn9.clicked.connect(lambda: self.clicker(self.btn9))
        self.btn10.clicked.connect(self.reset)

        # Show the App
        self.show()
    # Check Win
    def checkWin(self):
        # Across
        if (self.btn1.text()!="" and self.btn4.text()==self.btn7.text()==self.btn1.text()):
            self.Win(self.btn1, self.btn4, self.btn7)
        elif (self.btn2.text()!="" and self.btn5.text()==self.btn8.text()==self.btn2.text()):
            self.Win(self.btn2, self.btn5, self.btn8)
        elif (self.btn3.text()!="" and self.btn3.text()==self.btn6.text()==self.btn9.text()):
            self.Win(self.btn3, self.btn6, self.btn9)
        # Down
        elif (self.btn1.text()!="" and self.btn1.text()==self.btn2.text()==self.btn3.text()):
            self.Win(self.btn1, self.btn2, self.btn3)
        elif (self.btn4.text()!="" and self.btn4.text()==self.btn5.text()==self.btn6.text()):
            self.Win(self.btn4, self.btn5, self.btn6)
        elif (self.btn7.text()!="" and self.btn7.text()==self.btn8.text()==self.btn9.text()):
            self.Win(self.btn7, self.btn8, self.btn9)
        # Diagonal
        elif (self.btn1.text()!="" and self.btn1.text()==self.btn5.text()==self.btn9.text()):
            self.Win(self.btn1, self.btn5, self.btn9)
        elif (self.btn3.text()!="" and self.btn3.text()==self.btn5.text()==self.btn7.text()):
            self.Win(self.btn3, self.btn5, self.btn7)

    def Win(self, a, b, c):
        # Change the button color to red
        a.setStyleSheet('QPushButton {color : red}')
        b.setStyleSheet('QPushButton {color : red}')
        c.setStyleSheet('QPushButton {color : red}')
        # Add winner label
        self.mylabel.setText(f"{a.text()} Wins!")
        button_list = [self.btn1, 
                       self.btn2,
                       self.btn3,
                       self.btn4,
                       self.btn5,
                       self.btn6,
                       self.btn7,
                       self.btn8,
                       self.btn9]
        for button in button_list:
            button.setEnabled(False)


    # Click the Buttons
    def reset(self):
        button_list = [self.btn1, 
                       self.btn2,
                       self.btn3,
                       self.btn4,
                       self.btn5,
                       self.btn6,
                       self.btn7,
                       self.btn8,
                       self.btn9]
        for b in button_list:
            b.setText("")
            b.setEnabled(True)
            b.setStyleSheet('QPushButton {color : grey}')
        self.counter = 0
        self.mylabel.setText("X Goes First!")
    def clicker(self, btn):
        if self.counter%2==0:
            btn.setText("X")
            btn.setEnabled(False)
            if (self.counter!=8):
                self.mylabel.setText("O Goes Now!")
            else:
                self.mylabel.setText("It is Draw!")
            self.counter+=1
        else:
            btn.setText("O")
            btn.setEnabled(False)
            self.mylabel.setText("X Goes Now!")
            self.counter+=1
        self.checkWin()

app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()