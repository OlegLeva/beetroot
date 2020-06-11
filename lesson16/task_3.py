class Iterator:
    def __init__(self, *args):
        self.args = args
    def __iter__(self):
        return iter(self.args)
    def __getitem__(self, item):
        return self.args[item]

my_list = Iterator(1, 'u', 67, 'l', 555)

for i in my_list:
     print(i)

print(my_list[4])