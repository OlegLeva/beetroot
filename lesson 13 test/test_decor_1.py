from functools import wraps


def reverse_rec_file(filename1):
    def reverse_rec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            incoming_list = str((func(*args, **kwargs))[::-1])
            with open(filename1, "a") as fn1:
                fn1.write(incoming_list + "\n")
            return incoming_list
        return wrapper
    return reverse_rec


@reverse_rec_file("revers_list.txt")
def sort_list(random_list):
    list_1 = sorted(random_list)
    return list_1

sort_list([9, 5, 8, 3, 7])
print(help(sort_list))