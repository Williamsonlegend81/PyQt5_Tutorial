from typing_extensions import ReadOnly
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Learning PyQt5")

        # self.setLayout(qtw.QVBoxLayout())
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # Adding Stuffs/Widgets
        label_1 = qtw.QLabel("This is a Cool Label Row")
        label_1.setFont(qtg.QFont("Helvetica", 24))
        self.layout().addWidget(label_1)

        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)

        # Add rows to App
        form_layout.addRow(label_1)
        form_layout.addRow("First Name:",f_name)
        form_layout.addRow("Last Name:", l_name)
        form_layout.addRow(qtw.QPushButton("Press me!", clicked=lambda: press_it()))
        
        def press_it():
            label_1.setText(f"You clicked the Button, {f_name.text()} {l_name.text()}!")
        
        self.show()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()