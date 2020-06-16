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
