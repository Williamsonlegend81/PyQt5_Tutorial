from PyQt5.QtWidgets import QMainWindow, QLabel, QTextEdit, QPushButton, QApplication
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("Load.ui", self)

        # Define our Widgets
        self.label = self.findChild(QLabel, "label")
        self.textEdit = self.findChild(QTextEdit, "textEdit")
        self.pushButton = self.findChild(QPushButton, "pushButton")

        # Do something
        self.pushButton.clicked.connect(lambda: self.clicker())

        # Show the App
        self.show()
    def clicker(self):  
        self.label.setText(f"Hello, {self.textEdit.toPlainText()}")
        self.textEdit.setPlainText("")
# Initialize the app
app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()