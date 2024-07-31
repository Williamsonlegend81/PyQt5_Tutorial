import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a title
        self.setWindowTitle("Hello World")

        # Set Vertical layout
        self.setLayout(qtw.QVBoxLayout())
        
        # Create a Label
        my_label = qtw.QLabel("Hello World, What's your name")
        self.layout().addWidget(my_label)
        # Change the font size of label
        my_label.setFont(qtg.QFont("Helvetica",18))
        # Create a Entry Box

        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        # Create a Button

        my_button = qtw.QPushButton("Press Me", clicked=lambda:press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            # Add name to label
            my_label.setText(f"Hello, {my_entry.text()}")
            my_entry.setText("")

app = qtw.QApplication([])
mw = MainWindow()

# Run the app
app.exec_()