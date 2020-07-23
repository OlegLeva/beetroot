import psycopg2

connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                              user='postgres', password='levon4202099')
table_name = input("Enter table name for data entry: ")
if table_name == "country":
    def add_country():
        id = int(input("Enter id: "))
        country_name = input("The name of the country: ")
        abbr = input("Enter the abbreviation of the country: ")
        phone_code = input("Enter phone code: ")
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO country(id, country_name, abbr, phone_code) '
                       f'VALUES((%s), (%s), (%s), (%s))',
                       (id, country_name, abbr, phone_code))

        connection.commit()
        cursor.close()


    add_country()

if table_name == "city":
    def add_city():
        id = int(input("Enter id: "))
        city_name = input("The name of the city: ")
        country_id = input("Enter country_id: ")
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO city(id, city_name, country_id) '
                       f'VALUES((%s), (%s), (%s))',
                       (id, city_name, country_id))

        connection.commit()
        cursor.close()


    add_city()


if table_name == "person":
    def add_person():
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        city_id = input("Enter city_id: ")
        phone = input("Enter phone: ")
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO person(id, name, city_id, phone) '
                       f'VALUES((%s), (%s), (%s), (%s))',
                       (id, name, city_id, phone))

        connection.commit()
        cursor.close()


    add_person()
