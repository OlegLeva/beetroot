"""
import json

class PhoneBook():
    first_name = None
    last_name = None
    full_name = None
    phone = None
    region = None
    city = None

    def __init__(self, first_name, last_name, full_name, phone, region, city):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.phone = phone
        self.region = region
        self.city = city

    def __str__(self):
        return self.first_name, self.last_name, self.full_name, \
               self.phone, self.region, self.city

    def __repr__(self):
        return self.first_name, self.last_name, self.full_name, \
               self.phone, self.region, self.city

    def convert(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
            "phone": self.phone,
            "region": self.region,
            "city": self.city
        }

#    def inpt_name(self):
#        self.first_name = input('Enter first name: ').strip().lower().title()
#        self.last_name = input('Enter last name: ').strip().lower().title()
#        self.full_name = self.first_name + ' ' + self.last_name
#        self.phone = input('Enter phone: ')
#       self.region = input('Enter region: ').strip().lower().title()
#       self.city = input('Enter city: ').strip().lower().title()



new_ph = PhoneBook(first_name = input("), "last_name", "full_name", "phone", "region", "city")

new_list = new_ph.convert()

try:
    phb = json.load(open('test.json'))
except json.decoder.JSONDecodeError:
    phb = []


new_list = []
for item in phb:
    new_list.append(PhoneBook(**item))

new_list = [person.convert() for person in new_list]

with open("test.json", 'w') as f:
    json.dump(new_list, f, indent=4)

"""