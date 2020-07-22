import psycopg2

connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                              user='postgres', password='levon4202099')
id = int(input("Enter id: "))
first_name = input("Enter first_name: ")
last_name = input("Enter last_name: ")
full_name = input("Enter full_name: ")
phone = input("Enter phone: ")
region = input("Enter region: ")
city = input("Enter city: ")

cursor = connection.cursor()
cursor.execute(f'INSERT INTO public."Phonebook"(id, first_name, last_name, full_name, phone, region, city) '
               f'VALUES((%s), (%s), (%s), (%s), (%s), (%s), (%s))',
               (id, first_name, last_name, full_name, phone, region, city))
