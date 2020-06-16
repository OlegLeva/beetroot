"""
1. Импортируем JSON
2. Открываем файл
3. Ловим ошибки при открытии файла и создаём пустой список
4. Создаём шаблон словаря
5. Создаём try except глобальный
6. Внутри глобальнго try except создаём цикл с получением данных от пользователя
   с последующей записью в пустой словарь
7. Добавляем функции поиска, обновления данных по телефону,
   удаления элемента по телефону с JSON файла и выход из программы
8. добавляем файнели: после выхода с программы записываем все данные в файл JSON
9. создаю другой файл и запаковываю все действия в функции и импортируем их в программу.

"""
from typing import Dict, List, Tuple, Union, Optional, Any, AnyStr
import json

filename = "json1.json"
f = open(filename)

try:
    phb = json.load(f)
except json.decoder.JSONDecodeError:
    phb = []
f.close()

dict_pattern = {
    'first_name': '',
    'last_name': '',
    'full_name': '',
    'phone': '',
    'region': '',
    'city': ''
}


def add_f(lst, dct):
    first_name = input('Enter first name: ').strip().lower().title()
    last_name = input('Enter last name: ').strip().lower().title()
    full_name = first_name + ' ' + last_name
    phone = input('Enter phone: ')
    region = input('Enter region: ').strip().lower().title()
    city = input('Print city: ').strip().lower().title()
    new_dict = dct.copy()
    new_dict['first_name'] = first_name
    new_dict['last_name'] = last_name
    new_dict['full_name'] = full_name
    new_dict['phone'] = phone
    new_dict['region'] = region
    new_dict['city'] = city
    return lst.append(new_dict)


def search_first(n, dct):
    for i in dct:
        if i['first_name'] == n:
            print('Found person:')
            print(i)
            break

def search_last(n, dct):
    for i in dct:
        if i['last_name'] == n:
            print('Found person:')
            print(i)
            break


def search_full(n, dct):
    for i in dct:
        if i['full_name'] == n:
            print('Found person:')
            print(i)
            break


def search_phone(n, dct):
    for i in dct:
        if i['phone'] == n:
            print('Found person:')
            print(i)
            break


def search_citi(n, dct):
    for i in dct:
        if i['city'] == n:
            print('Found person:')
            print(i)
            break


def search_region(n, dct):
    for i in dct:
        if i['region'] == n:
            print('Found person:')
            print(i)
            break

def update_q(lst, n, dct):
    for item in dct:
        if item['phone'] == n:
            dct.remove(item)
            first_name = input('Enter first name: ').strip().lower().title()
            last_name = input('Enter last name: ').strip().lower().title()
            full_name = first_name + ' ' + last_name
            phone = input('Enter phone: ')
            region = input('Enter region: ').strip().lower().title()
            city = input('Print city: ').strip().lower().title()
            new_dict = lst.copy()
            new_dict['first_name'] = first_name
            new_dict['last_name'] = last_name
            new_dict['full_name'] = full_name
            new_dict['phone'] = phone
            new_dict['region'] = region
            new_dict['city'] = city
            dct.append(new_dict)
            break

def del_q(n, dct):
    for item in dct:
        if item['phone'] == n:
            dct.remove(item)
            break


try:
    while True:
        command = input('Select command: ').strip().lower()
        if command == 'add':
            add_f(phb, dict_pattern)

        elif command == 'search first name':
            query = input('First name: ').strip().lower().title()
            search_first(query, phb)

        elif command == 'search last name':
            query = input('Last name: ').strip().lower().title()
            search_last(query, phb)

        elif command == 'search full name':
            query = input('Full name: ').strip().lower().title()
            search_full(query, phb)

        elif command == 'search phone':
            query = input('Phone: ')
            search_phone(query, phb)

        elif command == 'search city':
            query = input('City: ').strip().lower().title()
            search_citi(query, phb)
        elif command == 'search region':
            query = input('Region: ').strip().lower().title()
            search_region(query, phb)

        elif command == 'exit':
            break
        elif command == 'update':
            query = input('Phone: ')
            update_q(dict_pattern, query, phb)

        elif command == 'delete':
            query = input('Phone: ')
            del_q(query, phb)


except Exception as e:
    print('Erorr')
    print(e)
finally:
    with open(filename, 'w') as f:
        json.dump(phb, f, indent=4)