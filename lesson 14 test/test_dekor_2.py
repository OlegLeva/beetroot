
def value_sq(x):
    def sq(func):
        def wrapper(a, b):
            return (func(a, b))**x
        return wrapper
    return sq

@value_sq(2)
def power(a, b):
    return a**b

print(power(3, 2))
