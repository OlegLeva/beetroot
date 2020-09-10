import psycopg2


def create_car_list():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "car_list" (id serial NOT NULL, car_numb varchar(8) NOT NULL, '
                   'trailer_numb varchar(8) NOT NULL, driver varchar(40) NOT NULL, '
                   'phone varchar(13) NOT NULL, PRIMARY KEY(id))')
    connection.commit()
    cursor.close()
    connection.close()


def create_car():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "car" (id int NOT NULL, TACHO date NOT NULL, PROTOKOL date NOT NULL, '
                   'car_list_id int NOT NULL, PRIMARY KEY(id))')
    connection.commit()
    cursor.close()
    connection.close()


def create_trailer():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "trailer" (id int NOT NULL, EKMT date NOT NULL, MSTO date NOT NULL, '
                   'Customs_sertificate date NOT NULL, car_id int NOT NULL, PRIMARY KEY(id))')
    connection.commit()
    cursor.close()
    connection.close()


def add_car_list():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')

    car_numb = input('Enter car number: ')
    trailer_numb = input('Enter trailer number: ')
    driver = input('Enter name driver: ')
    phone = input('Enter phone number: ')

    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO "car_list" (car_numb, trailer_numb, driver, phone)'
                   f'VALUES((%s), (%s), (%s), (%s))',
                   (car_numb, trailer_numb, driver, phone))
    connection.commit()
    cursor.close()
    connection.close()


# create_car_list()
# create_car()
# create_trailer()
add_car_list()
