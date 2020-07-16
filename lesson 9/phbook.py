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

import sys
import json
from task_2_func import add_f, search_id, search_first, search_last, search_full ,\
    search_phone, search_region, search_citi, update_q, del_q

filename = sys.argv[1]
f = open(filename)

try:
    phb = json.load(f)
except json.decoder.JSONDecodeError:
    phb = []
f.close()

dict_pattern = {
    'id': '',
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
            add_f(phb, dict_pattern)

        elif command == 'search id':
            query = input('id: ')
            search_id(query, phb)

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