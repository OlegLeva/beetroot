import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result
    return wrapper

def sq(func):
    def wrapper(*args, **kwargs):
        l1 = func(*args, **kwargs)
        l2 = [i ** 2 for i in l1]
        return l2
    return wrapper


def div(func):
    def wrapper(*args, **kwargs):
        l1 = func(*args, **kwargs)
        l2 = [i - 1 for i in l1]
        return l2
    return wrapper


def add_5b(func):
    def wrapper(*args, **kwargs):
        l1 = func(*args, **kwargs)
        l2 = [{"multiple_5": i} for i in l1 if i % 5 == 0]
        l3 = [{"multiple_3": i} for i in l1 if i % 3 == 0]
        return f"{l2}, \n{l3}"
    return wrapper



@add_5b
@div
@sq
@time_it
def get_list(list_arg):
    l = [x for x in list_arg if x % 2 == 0]
    return l

print(get_list(range(100**2)))
