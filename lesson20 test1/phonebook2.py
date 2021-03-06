
from typing import Dict, List, Union, Any
import json

filename = "json2.json"
f = open(filename)

try:
    phb: List[str] = json.load(f)
except json.decoder.JSONDecodeError:
    phb = []
f.close()

dict_pattern: Dict[str, str] = {
    'first_name': '',
    'last_name': '',
    'full_name': '',
    'phone': '',
    'region': '',
    'city': ''
}


def add_f(lst: Any, dct: Any) -> List:
    first_name: str = input('Enter first name: ').strip().lower().title()
    last_name: str = input('Enter last name: ').strip().lower().title()
    full_name: str = first_name + ' ' + last_name
    phone: str = input('Enter phone: ')
    region: str = input('Enter region: ').strip().lower().title()
    city: str = input('Print city: ').strip().lower().title()
    new_dict: Dict = dct.copy()
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
        else:
            return


def search_last(n, dct):
    for i in dct:
        if i['last_name'] == n:
            print('Found person:')
            print(i)
            break
        else:
            return


def search_full(n, dct):
    for i in dct:
        if i['full_name'] == n:
            print('Found person:')
            print(i)
            break
        else:
            return


def search_phone(n, dct):
    for i in dct:
        if i['phone'] == n:
            print('Found person:')
            print(i)
            break
        else:
            return


def search_citi(n, dct):
    for i in dct:
        if i['city'] == n:
            print('Found person:')
            print(i)
            break
        else:
            return


def search_region(n, dct):
    for i in dct:
        if i['region'] == n:
            print('Found person:')
            print(i)
            break
        else:
            return


def update_q(lst, n, dct):
    for item in dct:
        if item['phone'] == n:
            dct.remove(item)
            first_name: str = input('Enter first name: ').strip().lower().title()
            last_name: str = input('Enter last name: ').strip().lower().title()
            full_name: str = first_name + ' ' + last_name
            phone: Union[str, int] = input('Enter phone: ')
            region: str = input('Enter region: ').strip().lower().title()
            city: str = input('Print city: ').strip().lower().title()
            new_dict = lst.copy()
            new_dict['first_name'] = first_name
            new_dict['last_name'] = last_name
            new_dict['full_name'] = full_name
            new_dict['phone'] = phone
            new_dict['region'] = region
            new_dict['city'] = city
            dct.append(new_dict)
            break
        else:
            return


def del_q(n, dct):
    for item in dct:
        if item['phone'] == n:
            dct.remove(item)
            break
        else:
            return


try:
    while True:
        command = input('Select command: ').strip().lower()
        if command == 'add':
            add_f(phb, dict_pattern)

        elif command == '':
            query: Union[str, int] = input('First name: ').strip().lower().title()
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
