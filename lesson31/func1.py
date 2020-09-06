import psycopg2


def get_one():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM "Phonebook"')
    return cursor.fetchone()


print(get_one())


def get_all():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM "Phonebook"')
    return cursor.fetchall()


print(get_all())
