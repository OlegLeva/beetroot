from typing import Union


class Animal:
    def __init__(self, breed: str, nikname: str, age: Union [str, int]):
        self.breed = breed
        self.nikname = nikname
        if not (type(age) == str and age.isdigit()) and type(age) != int:
            raise ValueError(f'{age} must be an integer')
        self.age = age

    def getBreed(self):
        return self.breed

    def getNikname(self):
        return self.nikname

    def getAge(self):
        return self.age
