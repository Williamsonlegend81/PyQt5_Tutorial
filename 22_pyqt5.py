from PyQt5.QtWidgets import QMainWindow, QComboBox, QLabel, QApplication
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("dependent.ui", self)

        # Define our Widgets
        self.combo1 = self.findChild(QComboBox, "comboBox")
        self.combo2 = self.findChild(QComboBox,"comboBox_2")
        self.mylabel = self.findChild(QLabel, "label")

        # Add items to the Combo Box
        self.combo1.addItem("Male", ["John", "West", "Dan"])
        self.combo1.addItem("Female", ["April", "Steph", "Beth"])

        # Click the first dropdown
        self.combo1.activated.connect(self.clicker)
        self.combo2.activated.connect(self.clicker2)

        # Do something

        # Show the App
        self.show()
    def clicker(self, index):
        # Clear the second box
        self.combo2.clear()
        # Do the dependent thing
        self.combo2.addItems(self.combo1.itemData(index))
    def clicker2(self):
        self.mylabel.setText(f"You picked: {self.combo2.currentText()} - {self.combo1.currentText()}")
# Initialize the app
app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()