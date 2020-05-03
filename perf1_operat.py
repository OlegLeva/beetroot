


def add (x, y):
    return f'Addition: {float(x) + float(y)}'
def mult (x, y):
    return f'multiplication: {float(x) * float(y)}'
def div (x, y):
    if y == 0:
        return 'cannot be divided by (0)'
    return f'division: {float(x) / float(y)}'
def sub(x, y):
    return f'subtraction: {float(x) - float(y)}'
def divb(x, y):
    if y == 0:
        return 'cannot be divided by (0)'
    return f'division is complete: {float(x) // float(y)}'
def divby(x, y):
    if y == 0:
        return 'cannot be divided by (0)'
    return f'remainder of division of numbers: {float(x) % float(y)}'
def deg(x, y):
    return f'raise the number to the degree: {float(x) ** float(y)}'
def round(x, y):
    return f'round off the number: {round(float(x), int(y))}'
def bin(x):
    return f'Decimal converted to binary: {bin(int(x))}'
def addauto(x, y):
    return f'the sum of two numbers:  {int(x) + int(y)}'
def bit(x, y):
    return f'bitwise operation EXCLUSIVELY OR:  {int(x) ^ int(y)}'

"""oper = { '+': add(),
         '*': mult(),
         '/': div(),
         '-': sub(),
         '//': divb(),
         '%': divby(),
         '**': deg(),
         'r': round(),
         'b': bin(),
         's': addauto(),
         '^': bit()
         }"""
