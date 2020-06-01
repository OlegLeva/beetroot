def sq(func):
    l1 = func()

    def wrapper():
        l2 = [i ** 2 for i in l1]
        return l2

    return wrapper


def div(func):
    l1 = func()

    def wrapper():
        l2 = [i - 1 for i in l1]
        return l2

    return wrapper


def add_5b(func):
    l1 = func()

    def wrapper():
        l2 = [{"multiple_5": i} for i in l1 if i % 5 == 0]
        l3 = [{"multiple_3": i} for i in l1 if i % 3 == 0]
        return f"{l2}, \n{l3}"

    return wrapper


@add_5b
@div
@sq
def get_list():
    l = [x for x in range(100) if x % 2 == 0]
    return l

print(get_list())
