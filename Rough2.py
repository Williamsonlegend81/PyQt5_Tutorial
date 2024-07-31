import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Learning PyQt5")

        self.setLayout(qtw.QVBoxLayout())

        label_1 = qtw.QLabel("Hello user, I am learning PyQt5 with Codemy")
        label_1.setFont(qtg.QFont("Helvetica", 24))
        self.layout().addWidget(label_1)

        spin_box = qtw.QDoubleSpinBox(self,
                                maximum=100,
                                minimum=0,
                                value=10,
                                singleStep=5.5)
        spin_box.setFont(qtg.QFont("Helvetica", 18))
        self.layout().addWidget(spin_box)

        my_button = qtw.QPushButton("Press me!", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        def press_it():
            label_1.setText(f"Your current value {spin_box.value()}")
        
        self.show()

app = qtw.QApplication([])

mw = MainWindow()

app.exec_()