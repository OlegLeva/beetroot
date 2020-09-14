import psycopg2


def notification():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "Notification" (id int NOT NULL, days_before int NOT NULL,  '
                   'PRIMARY KEY(id))')
    connection.commit()
    cursor.close()
    connection.close()


def document():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "Document" (id int NOT NULL, exp_date Date NOT NULL,'
                   'name varchar(40) NOT NULL, truck_id varchar(8) NOT NULL,'
                   'driver_id varchar(13) NOT NULL, trailer_id varchar(8) NOT NULL,'
                   'PRIMARY KEY(id))')
    connection.commit()
    cursor.close()
    connection.close()


def truck():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "Truck" (license_plate varchar(8) NOT NULL, '
                   'PRIMARY KEY(license_plate))')
    connection.commit()
    cursor.close()
    connection.close()


def driver():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "Driver" (name varchar(40) NOT NULL, phone varchar(13) NOT NULL, '
                   'PRIMARY KEY(phone))')
    connection.commit()
    cursor.close()
    connection.close()


def trailer():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "Trailer" (license_plate varchar(8) NOT NULL, '
                   'PRIMARY KEY(license_plate))')
    connection.commit()
    cursor.close()
    connection.close()


def autoTrain():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "AutoTrain" (id serial NOT NULL,'
                   'truck_id varchar(8) NOT NULL, driver_id varchar(13) NOT NULL, '
                   'trailer_id varchar(8) NOT NULL, driver_name varchar(40) NOT NULL,'
                   'PRIMARY KEY(truck_id))')
    connection.commit()
    cursor.close()
    connection.close()


# notification()
# document()
# truck()
# trailer()
# driver()
autoTrain()