from functools import partial
import psycopg2
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QMainWindow,
                             QLabel,
                             QLineEdit,
                             QVBoxLayout,
                             QGridLayout,
                             QPushButton,
                             QSizePolicy,
                             QTextEdit)

import sys


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("DATABASE EDITOR ULTRA SUPER OFIGENNIY 2020")
        self.setGeometry(300, 100, 500, 400)
        widget = QWidget()
        self.digitLabel = QLabel('REQUEST')
        self.request = QLineEdit('')
        digitLabel_2 = QLabel('ANSWER')
        self.answer = QTextEdit('')

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.digitLabel)
        mainLayout.addWidget(self.request)
        mainLayout.addWidget(digitLabel_2)
        mainLayout.addWidget(self.answer)
        buttonLayout = QGridLayout()
        buttons = [
            {
                'name': 'create table country',
                'row': 0,
                'col': 0
            },
            {
                'name': 'create table city',
                'row': 0,
                'col': 1
            },
            {
                'name': 'create table person',
                'row': 0,
                'col': 2
            },
            {
                'name': 'get all',
                'row': 1,
                'col': 0
            },
            {
                'name': 'get data by name',
                'row': 1,
                'col': 1
            },
            {
                'name': 'Meditation',
                'row': 1,
                'col': 2
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
                                   )

        mainLayout.addLayout(buttonLayout)
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        self.buttons["get data by name"].clicked.connect(partial(self.get_phone_by_name))
        self.buttons["Meditation"].clicked.connect(partial(self.meditation))


    def meditation(self):
        self.answer.setText('OOOOOmmmmmmmmmmmmmmm...')


    def get_phone_by_name(self):
        try:
            connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                          user='postgres', password='levon4202099')
            self.name = self.request.text()
            cursor = connection.cursor()
            cursor.execute('SELECT city.city_name, person.name, country.phone_code, person.phone '
                           'FROM person '
                           'INNER JOIN city on  person.city_id = city.id '
                           'INNER JOIN country on city.country_id = country.id '
                           'WHERE name = \'%s\'' % self.name)
            s = ' '.join(map(str, cursor.fetchone()))
            self.answer.setText(s)
        except:
            self.answer.setText('No such name in the database')


def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
