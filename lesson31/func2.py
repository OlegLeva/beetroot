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
