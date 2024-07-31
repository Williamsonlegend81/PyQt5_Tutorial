from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("image_viewer.ui", self)

        # Add widgets to App
        self.label = self.findChild(QLabel, "label")
        self.btn = self.findChild(QPushButton, "pushButton")

        # Click the Dropdown box
        self.btn.clicked.connect(lambda: self.clicker())

        # Show the App
        self.show()
    def clicker(self):
        f_name = QFileDialog.getOpenFileName(self, "Open File", "d:\\Tkinter Tutorial\\Pokemon", "All files(*);; Png files(*.png);; JPEG files(*.jpeg)")

        # Open the image
        self.pixmap = QPixmap(f_name[0])
        # Add image to label
        self.label.setPixmap(self.pixmap)

app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()