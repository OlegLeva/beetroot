from functools import partial
import psycopg2
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QMainWindow,
                             QLabel,
                             QLineEdit,
                             QVBoxLayout,
                             QHBoxLayout,
                             QGridLayout,
                             QPushButton,
                             QSizePolicy,
                             QTextEdit)

import sys


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("DATABASE EDITOR")
        self.setGeometry(300, 100, 800, 500)
        widget = QWidget()
        # self.digitLabel = QLabel('REQUEST')
        self.request = QLineEdit('')
        self.request.setPlaceholderText("REQUEST")
        # self.digitLabel_2 = QLabel('ANSWER')
        self.answer = QTextEdit('')
        self.answer.setPlaceholderText("ANSWER")

        mostmaimlayout = QHBoxLayout()
        mainLayout = QVBoxLayout()
        mainLayout1 = QVBoxLayout()
        mostmaimlayout.addLayout(mainLayout)
        mostmaimlayout.addLayout(mainLayout1)
        # mainLayout.addWidget(self.digitLabel)
        mainLayout.addWidget(self.request)
        # mainLayout.addWidget(self.digitLabel_2)
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
        widget.setLayout(mostmaimlayout)
        self.setCentralWidget(widget)

        # self.digitLabel1 = QLabel('Enter country id')
        # mainLayout1.addWidget(self.digitLabel1)
        self.countryEdit1 = QLineEdit('')
        self.countryEdit1.setPlaceholderText('Enter country id')
        mainLayout1.addWidget(self.countryEdit1)

        # self.digitLabel2 = QLabel('Enter country name')
        # mainLayout1.addWidget(self.digitLabel2)
        self.countryEdit2 = QLineEdit('')
        self.countryEdit2.setPlaceholderText('Enter country name')
        mainLayout1.addWidget(self.countryEdit2)

        # self.digitLabel3 = QLabel('Enter country abbr')
        # mainLayout1.addWidget(self.digitLabel3)
        self.countryEdit3 = QLineEdit('')
        self.countryEdit3.setPlaceholderText('Enter country abbr')
        mainLayout1.addWidget(self.countryEdit3)

        # self.digitLabel4 = QLabel('Enter phone code')
        # mainLayout1.addWidget(self.digitLabel4)
        self.countryEdit4 = QLineEdit('')
        self.countryEdit4.setPlaceholderText('Enter phone code')
        mainLayout1.addWidget(self.countryEdit4)

        buttonLayout1 = QGridLayout()
        self.btn1 = QPushButton("Add country", self)
        self.btn1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        buttonLayout1.addWidget(self.btn1)
        mainLayout1.addLayout(buttonLayout1)

        # self.digitLabel11 = QLabel('Enter city id')
        # mainLayout1.addWidget(self.digitLabel11)
        self.countryEdit11 = QLineEdit('')
        self.countryEdit11.setPlaceholderText('Enter city id')
        mainLayout1.addWidget(self.countryEdit11)

        # self.digitLabel22 = QLabel('Enter city name')
        # mainLayout1.addWidget(self.digitLabel22)
        self.countryEdit22 = QLineEdit('')
        self.countryEdit22.setPlaceholderText('Enter city name')
        mainLayout1.addWidget(self.countryEdit22)

        # self.digitLabel33 = QLabel('Enter country id')
        # mainLayout1.addWidget(self.digitLabel33)
        self.countryEdit33 = QLineEdit('')
        self.countryEdit33.setPlaceholderText('Enter country id')
        mainLayout1.addWidget(self.countryEdit33)

        buttonLayout2 = QGridLayout()
        self.btn2 = QPushButton("Add city", self)
        self.btn2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        buttonLayout2.addWidget(self.btn2)
        mainLayout1.addLayout(buttonLayout2)

        # self.digitLabel111 = QLabel('Enter person id')
        # mainLayout1.addWidget(self.digitLabel111)
        self.countryEdit111 = QLineEdit('')
        self.countryEdit111.setPlaceholderText('Enter person id')
        mainLayout1.addWidget(self.countryEdit111)

        # self.digitLabel222 = QLabel('Enter name')
        # mainLayout1.addWidget(self.digitLabel222)
        self.countryEdit222 = QLineEdit('')
        self.countryEdit222.setPlaceholderText('Enter name')
        mainLayout1.addWidget(self.countryEdit222)

        # self.digitLabel333 = QLabel('Enter city id')
        # mainLayout1.addWidget(self.digitLabel333)
        self.countryEdit333 = QLineEdit('')
        self.countryEdit333.setPlaceholderText('Enter city id')
        mainLayout1.addWidget(self.countryEdit333)

        # Enter phone nomberainLayout1.addWidget(self.digitLabel444)
        self.countryEdit444 = QLineEdit('')
        self.countryEdit444.setPlaceholderText('Enter phone nomber')
        mainLayout1.addWidget(self.countryEdit444)

        buttonLayout3 = QGridLayout()
        self.btn3 = QPushButton("Add person", self)
        self.btn3.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        buttonLayout3.addWidget(self.btn3)
        mainLayout1.addLayout(buttonLayout3)

        self.buttons["get data by name"].clicked.connect(partial(self.get_phone_by_name))
        self.buttons["Meditation"].clicked.connect(partial(self.meditation))
        self.buttons["get all"].clicked.connect(partial(self.get_all))
        self.btn1.clicked.connect(partial(self.add_country))
        self.btn2.clicked.connect(partial(self.add_city))
        self.btn3.clicked.connect(partial(self.add_person))
        self.buttons["create table country"].clicked.connect(partial(self.create_country))
        self.buttons["create table city"].clicked.connect(partial(self.create_city))
        self.buttons["create table person"].clicked.connect(partial(self.create_person))

    def create_country(self):
        connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                      user='postgres', password='levon4202099')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE "country" (id int NOT NULL, country_name varchar(40) NOT NULL, '
                       'abbr varchar(3) NOT NULL, phone_code varchar(4) NOT NULL, PRIMARY KEY(id))')
        connection.commit()
        cursor.close()
        connection.close()

    def create_city(self):
        connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                      user='postgres', password='levon4202099')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE "city" (id int NOT NULL, city_name varchar(40) NOT NULL, '
                       'country_id int NOT NULL, PRIMARY KEY(id))')
        connection.commit()
        cursor.close()
        connection.close()

    def create_person(self):
        connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                      user='postgres', password='levon4202099')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE "person" (id int NOT NULL, name varchar(40) NOT NULL, '
                       'city_id int NOT NULL, PRIMARY KEY(id))')
        connection.commit()
        cursor.close()
        connection.close()

    def add_person(self):
        try:
            connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                          user='postgres', password='levon4202099')
            id = self.countryEdit111.text()
            name = self.countryEdit222.text()
            city_id = self.countryEdit333.text()
            phone = self.countryEdit444.text()

            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO person(id, name, city_id, phone)'
                           f'VALUES((%s), (%s), (%s), (%s))',
                           (id, name, city_id, phone))
            connection.commit()
            cursor.close()
            connection.close()
        except:
            self.answer.setText('Incorrectly entered data')

    def add_city(self):
        try:
            connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                          user='postgres', password='levon4202099')

            id = self.countryEdit11.text()
            city_name = self.countryEdit22.text()
            country_id = self.countryEdit33.text()

            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO city(id, city_name, country_id) '
                           f'VALUES((%s), (%s), (%s))',
                           (id, city_name, country_id))

            connection.commit()
            cursor.close()
            connection.close()
        except:
            self.answer.setText('Incorrectly entered data')

    def add_country(self):
        try:
            connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                          user='postgres', password='levon4202099')
            id = self.countryEdit1.text()
            country_name = self.countryEdit2.text()
            abbr = self.countryEdit3.text()
            phone_code = self.countryEdit4.text()

            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO country(id, country_name, abbr, phone_code) '
                           f'VALUES((%s), (%s), (%s), (%s))',
                           (id, country_name, abbr, phone_code))

            connection.commit()
            cursor.close()
            connection.close()
        except:
            self.answer.setText('Incorrectly entered data')

    def get_all(self):
        connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                      user='postgres', password='levon4202099')
        cursor = connection.cursor()
        cursor.execute('SELECT city.city_name, person.name, country.phone_code, person.phone '
                       'FROM person '
                       'INNER JOIN city on  person.city_id = city.id '
                       'INNER JOIN country on city.country_id = country.id ')
        s = ' '.join(map(str, cursor.fetchall()))
        print(s)
        self.answer.setText(s)

        connection.commit()
        cursor.close()
        connection.close()

    def meditation(self):
        self.answer.setText('OOOOOmmmmmmmmmmmmmmm...')

    def get_phone_by_name(self):
        try:
            connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                          user='postgres', password='levon4202099')
            name = self.request.text()
            cursor = connection.cursor()
            cursor.execute('SELECT city.city_name, person.name, country.phone_code, person.phone '
                           'FROM person '
                           'INNER JOIN city on  person.city_id = city.id '
                           'INNER JOIN country on city.country_id = country.id '
                           'WHERE name = \'%s\'' % name)
            s = ' '.join(map(str, cursor.fetchone()))
            self.answer.setText(s)
            connection.commit()
            cursor.close()
            connection.close()
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
