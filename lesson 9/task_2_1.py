"""
1. Импортируем JSON
2. Открываем файл
3. Ловим ошибки
4. Добавляю глобальный Try except
5. Создать функцию для добавления новых записей
6. Создать функцию для поиска по разным параметрам
7. Создать функцию для удаления и перезаписи записи по номеру телефона
8. Выход из программы
"""
import sys


json_file = open('phonebook.json', 'w')

import json

json_file = open('phonebook.json')
try:
    phonebook = json.load(json_file)
except json.decoder.JSONDecodeError:
    phonebook = []
json_file.close()
