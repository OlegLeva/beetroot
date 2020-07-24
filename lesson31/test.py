import psycopg2

'''SELECT  city.city_name, person.name, person.phone
FROM person
INNER JOIN city on  person.city_id = city.id
WHERE city_id = 2;'''

'''SELECT  city.city_name, person.name, country.phone_code, person.phone
FROM person
INNER JOIN city on  person.city_id = city.id
INNER JOIN country on city.country_id = country.id
WHERE city_id = 2;'''

'''SELECT  city.city_name, person.name, country.phone_code, person.phone
FROM person
INNER JOIN city on  person.city_id = city.id
INNER JOIN country on city.country_id = country.id
WHERE city_name = 'Kremenchuk' AND name = 'Olha'''


def get_citi_name_country_phone():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')
    cursor = connection.cursor()
    cursor.execute('SELECT  city.city_name, person.name, country.phone_code, person.phone '
                   'FROM person '
                   'INNER JOIN city on  person.city_id = city.id '
                   'INNER JOIN country on city.country_id = country.id '
                   'WHERE city_id = 2;')

    return cursor.fetchone()


print(get_citi_name_country_phone())


def get_phone_by_citi_name():
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                  user='postgres', password='levon4202099')
    city_name_in = input("Enter city: ")
    name_in = input("Enter name: ")
    cursor = connection.cursor()
    cursor.execute('SELECT city.city_name, person.name, country.phone_code, person.phone '
                   'FROM person '
                   'INNER JOIN city on  person.city_id = city.id '
                   'INNER JOIN country on city.country_id = country.id '
                   'WHERE city_name = \'%s\' AND name = \'%s\'' % (city_name_in, name_in))

    return cursor.fetchone()


print(get_phone_by_citi_name())
