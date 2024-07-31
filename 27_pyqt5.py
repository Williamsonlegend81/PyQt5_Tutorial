from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidget, QPushButton, QLineEdit, QInputDialog, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import Qt
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("list_widget.ui", self)

        # Add the Widgets
        self.addbtn = self.findChild(QPushButton, "Add_button")
        self.editbtn = self.findChild(QPushButton, "Edit_button")
        self.removebtn = self.findChild(QPushButton, "Remove_button")
        self.upbtn = self.findChild(QPushButton, "Up_button")
        self.downbtn = self.findChild(QPushButton, "Down_button")
        self.exitbtn = self.findChild(QPushButton, "Exit_button")
        self.sortbtn = self.findChild(QPushButton, "Sort_button")
        self.listwidget = self.findChild(QListWidget, "list_object")

        # Load the data into list widget
        self.listwidget.addItem("Delhi")
        self.listwidget.addItem("Mumbai")
        self.listwidget.addItem("Gandhinagar")
        self.listwidget.addItem("Ahmedabad")

        self.listwidget.setSelectionMode(QListWidget.SingleSelection)
        self.addbtn.clicked.connect(self.additem)
        self.editbtn.clicked.connect(self.edititem)
        self.removebtn.clicked.connect(self.removeitem)
        self.upbtn.clicked.connect(self.upitem)
        self.downbtn.clicked.connect(self.downitem)
        self.sortbtn.clicked.connect(self.sortitem)
        self.exitbtn.clicked.connect(self.exitpro)

        # Show the App
        self.show()
    def upitem(self):
        index = self.listwidget.currentRow()
        if index>=1:
            item = self.listwidget.takeItem(index)
            self.listwidget.insertItem(index-1, item)
            self.listwidget.setCurrentItem(item)
    def downitem(self):
        index = self.listwidget.currentRow()
        if (index<=self.listwidget.count()-1):
            item = self.listwidget.takeItem(index)
            self.listwidget.insertItem(index+1, item)
            self.listwidget.setCurrentItem(item)
    def sortitem(self):
        self.listwidget.sortItems()
    def exitpro(self):
        question = QMessageBox.question(self, "Exit the Program", "Do you want to quit the application?", QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            quit()
    def removeitem(self):
        currentindex = self.listwidget.currentRow()
        item = self.listwidget.item(currentindex)
        question = QMessageBox.question(self, "Remove City", "Do you want to remove this item on the list? " + item.text(), QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            item = self.listwidget.takeItem(currentindex)
            del item
    def edititem(self):
        currentindex = self.listwidget.currentRow()
        item = self.listwidget.item(currentindex)
        if item is not None:
            text, ok = QInputDialog.getText(self, "Edit City", "Enter City Name", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)
    def additem(self):
        currentindex = self.listwidget.currentRow()
        text, ok = QInputDialog.getText(self, "Add City", "City Name")
        if ok and text is not None:
            self.listwidget.insertItem(currentindex, text)
        

app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()