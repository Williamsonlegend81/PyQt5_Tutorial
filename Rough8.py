from PyQt5.QtWidgets import QMainWindow,QPushButton,QTextEdit,QFileDialog,QApplication
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
import json

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        # Load the UI file
        uic.loadUi("samplefile.ui",self)

        # Load the Widgets
        self.importfile = self.findChild(QPushButton,"pushButton")
        self.textbox = self.findChild(QTextEdit,"textEdit")

        self.importfile.clicked.connect(self.open_card)

        self.show()

    def open_card(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        filepath, _ = QFileDialog.getOpenFileName(self,"Open JSON File", "", "JSON Files(*.json);;All Files(*)")
        if filepath:
            try:
                with open(filepath,'r',encoding='utf-8') as f:
                    data = json.load(f)

                # Display the front data in textbox
                if 'front' in data:
                    self.textbox.setText(data['front'])
            except Exception as e:
                self.textbox.setText(f"Error reading file {e}")

app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()