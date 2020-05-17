
class Dog:
    age_factor = 7

    def __init__(self, age_factor):
        self.age_factor = age_factor

    def human_age(self):
        h_age = self.age_factor * 7
        return f"Dog age in human terms: {h_age}"


dvor_terrier = Dog(5)
mops = Dog(10)

print(dvor_terrier.human_age())
print(mops.human_age())