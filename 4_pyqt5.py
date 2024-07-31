from logging import PlaceHolder
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Learning PyQt5")

        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("Type Something in box below")

        my_label.setFont(qtg.QFont("Helvetica", 24))
        self.layout().addWidget(my_label)

        my_text = qtw.QTextEdit(self,
                                lineWrapMode = qtw.QTextEdit.FixedColumnWidth,
                                plainText = "This is real text",
                                acceptRichText = True,
                                lineWrapColumnOrWidth=50,
                                placeholderText="Hello World!",
                                readOnly=True)
        my_text.resize(400,400)
        self.layout().addWidget(my_text)

        my_button = qtw.QPushButton("Press me!", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        def press_it():
            my_label.setText(f"You typed {my_text.toPlainText()}")
            my_text.setPlainText("You typed")
        
        self.show()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()