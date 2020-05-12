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

"""

import json


f = open("myphonebook.json")

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

try:
    while True:
        command = input('Select command: ').strip().lower()
        if command == 'add':
            first_name = input('Enter first name: ').strip().lower().title()
            last_name = input('Enter last name: ').strip().lower().title()
            full_name = first_name + ' ' + last_name
            phone = input('Enter phone: ')
            region = input('Enter region: ').strip().lower().title()
            city = input('Print city: ').strip().lower().title()
            new_dict = dict_pattern.copy()
            new_dict['first_name'] = first_name
            new_dict['last_name'] = last_name
            new_dict['full_name'] = full_name
            new_dict['phone'] = phone
            new_dict['region'] = region
            new_dict['city'] = city
            phb.append(new_dict)
        elif command == 'search first name':
            query = input('First name: ').strip().lower().title()
            for item in phb:
                if item['first_name'] == query:
                    print('Found person:')
                    print(item)
                    break
        elif command == 'search last name':
            query = input('Last name: ').strip().lower().title()
            for item in phb:
                if item['last_name'] == query:
                    print('Found person:')
                    print(item)
                    break
        elif command == 'search full name':
            query = input('Full name: ').strip().lower().title()
            for item in phb:
                if item['full_name'] == query:
                    print('Found person:')
                    print(item)
                    break
        elif command == 'search phone':
            query = input('Phone: ')
            for item in phb:
                if item['phone'] == query:
                    print('Found person:')
                    print(item)
                    break
        elif command == 'search city':
            query = input('City: ').strip().lower().title()
            for item in phb:
                if item['city'] == query:
                    print('Found person:')
                    print(item)
                    break
        elif command == 'search region':
            query = input('Region: ').strip().lower().title()
            for item in phb:
                if item['region'] == query:
                    print('Found person:')
                    print(item)
                    break
        elif command == 'exit':
            break
        elif command == 'update':
            query = input('Phone: ')
            for item in phb:
                if item['phone'] == query:
                    phb.remove(item)
                    first_name = input('Enter first name: ').strip().lower().title()
                    last_name = input('Enter last name: ').strip().lower().title()
                    full_name = first_name + ' ' + last_name
                    phone = input('Enter phone: ')
                    region = input('Enter region: ').strip().lower().title()
                    city = input('Print city: ').strip().lower().title()
                    new_dict = dict_pattern.copy()
                    new_dict['first_name'] = first_name
                    new_dict['last_name'] = last_name
                    new_dict['full_name'] = full_name
                    new_dict['phone'] = phone
                    new_dict['region'] = region
                    new_dict['city'] = city
                    phb.append(new_dict)
                    break
        elif command == 'delete':
            query = input('Phone: ')
            for item in phb:
                if item['phone'] == query:
                    phb.remove(item)
                    break


except Exception as e:
    print('Erorr')
    print(e)
finally:
    with open('myphonebook.json', 'w') as f:
        json.dump(phb, f, indent=4)