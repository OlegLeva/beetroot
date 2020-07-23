'''SELECT  city.city_name, person.name, person.phone
FROM person
INNER JOIN city on  person.city_id = city.id
WHERE city_id = 2;'''

'''SELECT  city.city_name, person.name, country.phone_code, person.phone
FROM person
INNER JOIN city on  person.city_id = city.id
INNER JOIN country on city.country_id = country.id
WHERE city_id = 2;'''