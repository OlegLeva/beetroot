
class Person:

    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.last_name} {self.first_name} and I’m {self.age} years old”')


person1 = Person(last_name="Carl", first_name="Johnson", age=26)

print(person1.talk())