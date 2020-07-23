import psycopg2

connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                              user='postgres', password='levon4202099')


def create_country():
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "country" (id int, country_name varchar(40), abbr varchar(3), phone_code varchar(4))')
    connection.commit()
    cursor.close()
    connection.close()


def create_city():
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "city" (id int, city_name varchar(40), country_id int)')
    connection.commit()
    cursor.close()
    connection.close()


def create_person():
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "person" (id int, name varchar(40), city_id int)')
    connection.commit()
    cursor.close()
    connection.close()


create_country()
