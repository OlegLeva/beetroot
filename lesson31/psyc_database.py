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
                             QSizePolicy)

import sys


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("DATABASE EDITOR ULTRA SUPER OFIGENNIY 2020")
        self.setGeometry(300, 100, 500, 700)
        widget = QWidget()
        self.digitLabel = QLabel('REQUEST')
        self.request = QLineEdit('')
        digitLabel_2 = QLabel('ANSWER')
        self.answer = QLineEdit('')

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
                                   buttonConfig.get('col'))

        mainLayout.addLayout(buttonLayout)
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        self.digitLabel1 = QLabel('Enter country id')
        mainLayout.addWidget(self.digitLabel1)
        self.countryEdit1 = QLineEdit('')
        mainLayout.addWidget(self.countryEdit1)

        self.digitLabel2 = QLabel('Enter country name')
        mainLayout.addWidget(self.digitLabel2)
        self.countryEdit2 = QLineEdit('')
        mainLayout.addWidget(self.countryEdit2)

        self.digitLabel3 = QLabel('Enter country abbr')
        mainLayout.addWidget(self.digitLabel3)
        self.countryEdit3 = QLineEdit('')
        mainLayout.addWidget(self.countryEdit3)

        self.digitLabel4 = QLabel('Enter phone code')
        mainLayout.addWidget(self.digitLabel4)
        self.countryEdit4 = QLineEdit('')
        mainLayout.addWidget(self.countryEdit4)

        buttonLayout1 = QGridLayout()
        btn1 = QPushButton("Add country", self)
        btn1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        buttonLayout1.addWidget(btn1)
        mainLayout.addLayout(buttonLayout1)

        self.digitLabel11 = QLabel('Enter city id')
        mainLayout.addWidget(self.digitLabel11)
        self.countryEdit11 = QLineEdit('')
        mainLayout.addWidget(self.countryEdit11)

        self.digitLabel22 = QLabel('Enter city name')
        mainLayout.addWidget(self.digitLabel22)
        self.countryEdit22 = QLineEdit('')
        mainLayout.addWidget(self.countryEdit22)

        self.digitLabel33 = QLabel('Enter country id')
        mainLayout.addWidget(self.digitLabel33)
        self.countryEdit33 = QLineEdit('')
        mainLayout.addWidget(self.countryEdit33)

        buttonLayout2 = QGridLayout()
        btn2 = QPushButton("Add city", self)
        btn2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        buttonLayout2.addWidget(btn2)
        mainLayout.addLayout(buttonLayout2)

        self.digitLabel111 = QLabel('Enter person id')
        mainLayout.addWidget(self.digitLabel111)
        self.countryEdit111 = QLineEdit('')
        mainLayout.addWidget(self.countryEdit111)

        self.digitLabel222 = QLabel('Enter name')
        mainLayout.addWidget(self.digitLabel222)
        self.countryEdit222 = QLineEdit('')
        mainLayout.addWidget(self.countryEdit222)

        self.digitLabel333 = QLabel('Enter city id')
        mainLayout.addWidget(self.digitLabel333)
        self.countryEdit333 = QLineEdit('')
        mainLayout.addWidget(self.countryEdit333)

        self.digitLabel444 = QLabel('Enter phone nomber')
        mainLayout.addWidget(self.digitLabel444)
        self.countryEdit444 = QLineEdit('')
        mainLayout.addWidget(self.countryEdit444)

        buttonLayout3 = QGridLayout()
        btn3 = QPushButton("Add person", self)
        btn3.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        buttonLayout3.addWidget(btn3)
        mainLayout.addLayout(buttonLayout3)

        self.buttons["get data by name"].clicked.connect(partial(self.get_phone_by_name))
        self.buttons["Meditation"].clicked.connect(partial(self.meditation))
        self.buttons["get all"].clicked.connect(partial(self.get_all))

    def get_all(self):
        connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                      user='postgres', password='levon4202099')
        self.name = self.request.text()
        cursor = connection.cursor()
        cursor.execute('SELECT city.city_name, person.name, country.phone_code, person.phone '
                       'FROM person '
                       'INNER JOIN city on  person.city_id = city.id '
                       'INNER JOIN country on city.country_id = country.id ')
        s = ' '.join(map(str, cursor.fetchall()))
        print(s)
        self.answer.setText(s)


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
