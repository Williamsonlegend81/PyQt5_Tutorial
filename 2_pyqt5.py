import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a title
        self.setWindowTitle("Hello World")

        # Set a Vertical Layout

        self.setLayout(qtw.QVBoxLayout())
        # Create a Label

        my_label = qtw.QLabel("Pick something From the list")
        self.layout().addWidget(my_label)
        my_label.setFont(qtg.QFont("Helvetica", 18))
        
        my_entry = qtw.QLineEdit(self)
        my_entry.setObjectName("name_field")
        # Create a Combo Boxes
        combo_box = qtw.QComboBox(self,editable=True,insertPolicy=qtw.QComboBox.InsertPolicy.InsertAtBottom)

        # Add items to the combo box  
        combo_box.addItem("Pepperoni", "Something")
        combo_box.addItem("Cheese", 2)
        combo_box.addItem("Mushroom", qtw.QWidget)
        combo_box.addItem("Pepper")
        combo_box.addItems(["One","Two","Three"])
        combo_box.insertItem(2, "Third Thing")

        self.layout().addWidget(combo_box)
              

        # Create a button
        my_button = qtw.QPushButton(text="Press me", clicked=lambda: pressed())
        self.layout().addWidget(my_button)

        def pressed():
            my_label.setText(f"You picked, {combo_box.currentText()}")

        self.show()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
