
class Iterator:
    def __init__(self, *args):
        self.args = args
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.args):
            raise StopIteration
        value = self.args[self.index]
        value += 1
        return value

my_list = [1, 'u', 67, 'l', 555]
my_tuple = 3, 7, 0, 22, 90

t = iter(my_tuple)
l = my_list

for i in l:
    print(i)

for i in l:
    print(i)

for i in t:
    print(i)

for i in t:
    print(i)