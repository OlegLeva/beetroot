class Animal:
    def __init__(self, breed: str, nikname: str, age: int):
        self.breed = breed
        self.nikname = nikname
        self.age = age

    def getBreed(self):
        return self.breed

    def getNikname(self):
        return self.nikname

    def getAge(self):
        return self.age
