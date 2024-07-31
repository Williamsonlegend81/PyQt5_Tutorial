from PyQt5.QtWidgets import QLabel, QPushButton, QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("dialog.ui", self)

        # Add Widgets to the App
        self.mylabel = self.findChild(QLabel, "label")
        self.pushButton = self.findChild(QPushButton, "pushButton")

        # Click the button
        self.pushButton.clicked.connect(self.clicker)

        # Show the App
        self.show()
    def clicker(self):
        # Open File Dialog
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Python Files (*.py)")

        # Output Filename to screen
        if fname:
            self.mylabel.setText(f"File path: {fname[0]}")



app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()