import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Learning PyQt5")

        self.setLayout(qtw.QVBoxLayout())
        my_label = qtw.QLabel("Hello, I am learning PyQt5")
        self.layout().addWidget(my_label)

        my_label.setFont(qtg.QFont("Helvetica", 18))

        my_spin = qtw.QSpinBox(self, value=10, maximum=100, minimum=0, singleStep=5, prefix='#', suffix=" Order")
        my_spin.setFont(qtg.QFont("Helvetica", 18))
        self.layout().addWidget(my_spin)
        my_button = qtw.QPushButton("Press me", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        def press_it():
            my_label.setText(f"You pressed {my_spin.value()}")
        self.show()


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()

