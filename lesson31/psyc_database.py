from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QMainWindow,
                             QLabel,
                             QLineEdit,
                             QVBoxLayout,
                             QGridLayout,
                             QTextEdit)

import sys


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("DATABASE EDITOR ULTRA SUPER OFIGENNIY 2020")
        self.setGeometry(300, 100, 500, 400)
        widget = QWidget()
        digitLabel = QLabel('REQUEST')
        self.editArea = QLineEdit('')
        digitLabel_2 = QLabel('ANSWER')
        self.answer = QTextEdit('')


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(digitLabel)
        mainLayout.addWidget(self.editArea)
        mainLayout.addWidget(digitLabel_2)
        mainLayout.addWidget(self.answer)
        buttonLayout = QGridLayout()

        mainLayout.addLayout(buttonLayout)
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)




def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()