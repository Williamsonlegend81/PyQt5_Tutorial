from PyQt5.QtWidgets import QMainWindow, QTextEdit, QLabel, QPushButton,QApplication
from PyQt5 import uic
import json
import os
import time
import sys

class ThirdUI(QMainWindow):
    def __init__(self):
        super(ThirdUI, self).__init__()

        # Load the ui file
        uic.loadUi("rough3.ui", self)

        # Load the widgets
        self.question1 = self.findChild(QTextEdit, "textEdit")
        self.question2 = self.findChild(QTextEdit, "textEdit_2")
        self.message = self.findChild(QLabel, "label")
        self.showanswer = self.findChild(QPushButton, "pushButton_5")
        self.option1 = self.findChild(QPushButton, "pushButton")
        self.option2 = self.findChild(QPushButton, "pushButton_2")
        self.option3 = self.findChild(QPushButton, "pushButton_3")
        self.option4 = self.findChild(QPushButton, "pushButton_4")
        self.congrats = self.findChild(QLabel, "label_2")
        self.closing = self.findChild(QPushButton, "pushButton_6")
        self.option1.hide()
        self.option2.hide()
        self.option3.hide()
        self.option4.hide()
        self.question2.hide()
        self.congrats.hide()
        self.closing.hide()

        # Activating the functions
        # self.showanswer.clicked.connect(self.show_answer)
        # self.option1.clicked.connect(self.next_card)
        # self.option2.clicked.connect(self.next_card)
        # self.option3.clicked.connect(self.next_card)
        # self.option4.clicked.connect(self.next_card)
        # self.closing.clicked.connect(lambda: self.show_main(main_w, counter))

        # self.cards = []
        # self.current_card_index = 0
        # self.load_deck_data(list_widget)

        # self.start_time = time.time()

        # Set dark mode
        self.set_dark_mode()
        self.show()

    # def load_deck_data(self, list_widget):
    #     for lister in list_widget:
    #         folder_name = lister
    #         self.load_cards_from_folder(folder_name)
    #     self.load_card()

    # def show_main(self, main_w, number):
    #     t2 = time.time() - self.start_time
    #     main_w.timelabel.setText(f"Studied {number} cards in {t2:.2f} seconds today {(t2 / number):.2f} s/cards")
    #     lst_new = main_w.new
    #     lst_learn = main_w.learn
    #     lst_items = main_w.listwidget
    #     for i in range(lst_learn.count()):
    #         lst_learn.item(i).setText(f"{len(os.listdir(lst_items.item(i).text()))}")
    #     for i in range(lst_new.count()):
    #         lst_new.item(i).setText("0")
    #     main_w.show()
        # self.close()

    # def load_cards_from_folder(self, folder_name):
    #     folder_path = os.path.join("d:\\PyQt5 tutorial", folder_name)
    #     if os.path.isdir(folder_path):
    #         for filename in os.listdir(folder_path):
    #             if filename.endswith('.json'):
    #                 filepath = os.path.join(folder_path, filename)
    #                 with open(filepath, "r", encoding='utf-8') as f:
    #                     card_data = json.load(f)
    #                     self.cards.append(card_data)

    # def load_card(self):
    #     if not self.cards:
    #         self.message.setText("No cards available")
    #         return

    #     card = self.cards[self.current_card_index]
    #     self.question1.setText(card['front'])
    #     self.question2.setText(card['back'])
    #     self.question2.hide()
    #     self.showanswer.show()
    #     self.option1.hide()
    #     self.option2.hide()
    #     self.option3.hide()
    #     self.option4.hide()

    # def show_answer(self):
    #     self.question2.show()
    #     self.showanswer.hide()
    #     self.option1.show()
    #     self.option2.show()
    #     self.option3.show()
    #     self.option4.show()

    # def next_card(self):
    #     self.current_card_index += 1
    #     if self.current_card_index >= len(self.cards):
    #         self.showanswer.hide()
    #         self.congrats.show()
    #         self.question1.hide()
    #         self.question2.hide()
    #         self.option1.hide()
    #         self.option2.hide()
    #         self.option3.hide()
    #         self.option4.hide()
    #         self.message.hide()
    #         self.closing.show()
    #     else:
    #         self.load_card()

    def set_dark_mode(self):
        dark_style = """
            QMainWindow {
                background-color: #2d2d2d;
                color: #ffffff;
            }
            QTextEdit {
                background-color: #3c3c3c;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
            QPushButton {
                background-color: #5c5c5c;
                color: #ffffff;
                border: 1px solid #3c3c3c;
            }
            QPushButton::hover {
                background-color: #6c6c6c;
            }
        """
        self.setStyleSheet(dark_style)
        self.question1.setStyleSheet(dark_style)
        self.question2.setStyleSheet(dark_style)
        self.message.setStyleSheet(dark_style)
        self.congrats.setStyleSheet(dark_style)

app = QApplication(sys.argv)

UIWindow = ThirdUI()

app.exec_()