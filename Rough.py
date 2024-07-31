import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")

        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        label_1 = qtw.QLabel("Enter your name in here")
        label_1.setFont(qtg.QFont("Helvetica, 24"))
        self.layout().addWidget(label_1)

        entry_1 = qtw.QLineEdit(self)
        form_layout.addRow("First_name", entry_1)

        entry_2 = qtw.QLineEdit(self)
        form_layout.addRow("Last_name", entry_2)

        my_text = qtw.QTextEdit(self, 
                                lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                                lineWrapColumnOrWidth = 100,
                                acceptRichText=True,
                                placeholderText="Hello, write here",
                                plainText="This how it looks")
        form_layout.addRow(my_text)

        my_button = qtw.QPushButton("Press Me!", clicked=lambda: press_it())
        form_layout.addRow(my_button)
        
        label_3 = qtw.QLabel("This is how it looks")
        label_3.setFont(qtg.QFont("Helvetica", 24))
        self.layout().addWidget(label_3)

        def press_it():
            label_1.setText(f"Welcome {entry_1.text()} {entry_2.text()}")
            entry_1.setText("")
            entry_2.setText("")
            label_3.setText(f"You typed {my_text.toPlainText()}")
            

        self.show()

app = qtw.QApplication([])

mw = MainWindow()

app.exec_()