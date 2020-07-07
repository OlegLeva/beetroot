#За основу взял калькулятор iPhone

import sys
from decimal import Decimal
from math import sqrt
from functools import partial
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QVBoxLayout,
                             QGridLayout,
                             QLineEdit,
                             QMainWindow,
                             QPushButton,
                             QLabel,
                             QSizePolicy)


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Calculator 1.2')
        self.setGeometry(300, 100, 500, 400)
        widget = QWidget()
        digitLabel = QLabel('∞-DIGIT')
        self.editArea = QLineEdit('')

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(digitLabel)
        mainLayout.addWidget(self.editArea)
        buttonLayout = QGridLayout()
        buttons = [
            {
                'name': 'AC',
                'row': 0,
                'col': 0
            },
            {
                'name': '√',
                'row': 0,
                'col': 1
            },
            {
                'name': '%',
                'row': 0,
                'col': 2
            },
            {
                'name': '/',
                'row': 0,
                'col': 3
            },
            {
                'name': '7',
                'row': 1,
                'col': 0
            },
            {
                'name': '8',
                'row': 1,
                'col': 1
            },
            {
                'name': '9',
                'row': 1,
                'col': 2
            },
            {
                'name': '*',
                'row': 1,
                'col': 3
            },
            {
                'name': '4',
                'row': 2,
                'col': 0
            },
            {
                'name': '5',
                'row': 2,
                'col': 1
            },
            {
                'name': '6',
                'row': 2,
                'col': 2
            },
            {
                'name': '-',
                'row': 2,
                'col': 3
            },
            {
                'name': '1',
                'row': 3,
                'col': 0
            },
            {
                'name': '2',
                'row': 3,
                'col': 1
            },
            {
                'name': '3',
                'row': 3,
                'col': 2
            },
            {
                'name': '+',
                'row': 3,
                'col': 3
            },
            {
                'name': '0',
                'row': 4,
                'col': 0,
                'colSpan': 2
            },
            {
                'name': '.',
                'row': 4,
                'col': 2
            },
            {
                'name': '=',
                'row': 4,
                'col': 3
            },

        ]
        self.buttons = {}
        for buttonConfig in buttons:
            name = buttonConfig.get('name', '')
            btn = QPushButton(name)
            btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
            self.buttons[name] = btn
            buttonLayout.addWidget(btn,
                                   buttonConfig.get('row'),
                                   buttonConfig.get('col'),
                                   1,
                                   buttonConfig.get('colSpan', 1))

        mainLayout.addLayout(buttonLayout)
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        # digit buttons clicks
        for buttonName in '0123456789':
            btn = self.buttons[buttonName]
            btn.clicked.connect(partial(self.on_digit_click, buttonName))

        # equals button
        self.buttons["="].clicked.connect(self.on_equals_click)
        # comma
        self.buttons["."].clicked.connect(self.on_comma_click)
        # AC
        self.buttons["AC"].clicked.connect(self.init_state)
        # √
        self.buttons["%"].clicked.connect(self.on_percent_click)

        # +-*/ buttons
        for buttonName in '+-*/√':
            btn = self.buttons[buttonName]
            btn.clicked.connect(partial(self.on_operation_click, buttonName))

        self.init_state()

    def init_state(self):
        # init internal state
        self.display_string = "0"
        self.current_operation = None
        self.need_reset_display = False
        self.result = 0
        self.display()

    def reset_display(self):
        self.display_string = "0"
        self.need_reset_display = False

    def display(self):
        """ Displays internal display_string """
        self.editArea.setText("")
        self.editArea.setText(self.display_string)

    def on_digit_click(self, digit):
        if self.need_reset_display:
            self.reset_display()

        if self.display_string == "0":
            self.display_string = digit
        else:
            self.display_string += digit
        self.display()

    def on_comma_click(self):
        if "." not in self.display_string:
            self.display_string += "."

    @property
    def display_value(self):
        if "." in self.display_string:
            res = Decimal(self.display_string)
        else:
            res = int(self.display_string)
        return res

    def on_equals_click(self):
        try:
            if self.current_operation:
                if self.current_operation == "+":
                    self.result += self.display_value
                elif self.current_operation == "-":
                    self.result -= self.display_value
                elif self.current_operation == "*":
                    self.result *= self.display_value
                elif self.current_operation == "/":
                    self.result /= self.display_value
                elif self.current_operation == "√":
                    self.result = sqrt(self.display_value)

                self.current_operation = None
                self.display_string = str(self.result)
                self.display()
        except ZeroDivisionError:
            print("You cannot divide by zero!")

    def on_percent_click(self):
        try:
            if self.current_operation:
                if self.current_operation == "+":
                    self.result = self.result + ((self.result/100)*self.display_value)
                elif self.current_operation == "-":
                    self.result = self.result - ((self.result / 100) * self.display_value)
                elif self.current_operation == "*":
                    self.result = (self.result / 100) * self.display_value
                elif self.current_operation == "/":
                    self.result = self.result * (100 / self.display_value)

                self.current_operation = None
                self.display_string = str(self.result)
                self.display()
        except ZeroDivisionError:
            print("You cannot divide by zero!")


    def on_operation_click(self, operation):
        if self.current_operation and not self.need_reset_display:
            self.on_equals_click()

        self.result = self.display_value
        self.need_reset_display = True
        self.current_operation = operation


def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()