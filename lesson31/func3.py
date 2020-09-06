import psycopg2

connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                              user='postgres', password='levon4202099')


def create_country():
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "country" (id int NOT NULL, country_name varchar(40) NOT NULL, '
                   'abbr varchar(3) NOT NULL, phone_code varchar(4) NOT NULL, PRIMARY KEY(id))')
    connection.commit()
    cursor.close()
    connection.close()



def create_city():
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "city" (id int NOT NULL, city_name varchar(40) NOT NULL, '
                   'country_id int NOT NULL, PRIMARY KEY(id))')
    connection.commit()
    cursor.close()
    connection.close()


def create_person():
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "person" (id int NOT NULL, name varchar(40) NOT NULL, '
                   'city_id int NOT NULL, PRIMARY KEY(id))')
    connection.commit()
    cursor.close()
    connection.close()



