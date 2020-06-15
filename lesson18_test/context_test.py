import os
from contextlib import contextmanager

class File:
    def __init__(self, file_name):
        if os.path.exists(file_name):
            self.__file = open(file_name, encoding="utf-8")
        else:
            ValueError(f"Де їй взятися {file_name}")

    def __enter__(self):
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file.close()

with File("text.txt") as f:
    print(f.read())

class MutabelList:
    def __init__(self, data):
        self.list = data
        self.__local_list = data[:]


    def __enter__(self):
        return self.list

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.list = self.__local_list[:]

temp_data = MutabelList([1,2,3,4])
print(temp_data.list)
with temp_data as f:
    f.append(5)
    print(f)
print(temp_data.list)

@contextmanager
def open_file(file_name):
    file = open(file_name, encoding="utf-8")
    yield file
    file.close()

with open_file("text.txt") as f:
    print(f.read())


def file_raise(file_name):
    file = open(file_name, encoding="utf-8")
    try:
        yield file
    finally:
        file.close()

try:
    with open_file("text.txt") as f:
        raise ValueError
        print(f.read())
except:
    pass

