class Animal:

    @staticmethod
    def run():
        return "go"

dog = Animal()

print(Animal.run())
print(dog.run())
