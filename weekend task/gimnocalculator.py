
# calculator with a question

name = input('Please enter your name: ')

# Brings a name to a normal format. Subject to suddenly a double name.
import check_namemenu
check_namemenu.menu(name)

# syntax check
from val_conv5 import val_conv

def operation(a, b):
    '''mathematical operations with two data'''
    x = val_conv(a)
    y = val_conv(b)
    if operator == '+':
        if x is None or y is None:
            return None
        return (f'Addition: {float(x) + float(y)}')
    if operator == '*':
        if x is None or y is None:
            return None
        return (f'multiplication: {float(x) * float(y)}')
    if operator == '/':
        if x is None or y is None:
            return None
        return (f'division: {float(x) / float(y)}')
    if operator == '-':
        if x is None or y is None:
            return None
        return (f'subtraction: {float(x) - float(y)}')
    if operator == '//':
        if x is None or y is None:
            return None
        return (f'division is complete: {float(x) // float(y)}')
    if operator == '%':
        if x is None or y is None:
            return None
        return (f'remainder of division of numbers: {float(x) % float(y)}')
    if operator == '**':
        if x is None or y is None:
            return None
        return (f'raise the number to the degree: {float(x) ** float(y)}')
    if operator == 'r':
        if x is None or y is None:
            return None
        return (f'round off the number: {round(float(x), int(y))}')
    if operator == 'b':
        if x is None or y is None:
            return None
        return (f'Decimal converted to binary: {bin(int(x))}')
    if operator == 's':
        if x is None or y is None:
            return None
        return (f'the sum of two numbers:  {int(x) + int(y)}')
    if operator == '^':
        if x is None or y is None:
            return None
        return (f'bitwise operation EXCLUSIVELY OR:  {int(x) ^ int(y)}')

def one_x(a):
    '''mathematical operations with one input'''
    x = val_conv(a)
    if operator == 'sq':
        if x is None:
            return None
        return (f'The square root of the number is: {float(x) **(1/2)}')
    if operator == 'sqrt':
        from math import sqrt
        if x is None:
            return None
        return (f'square root: {sqrt(x)}')


while True:
    '''input processing'''
    operator = input(f'please select the operation you need: ')
    operator = operator.replace(" ", "")
    tup_op = ('+', '*', '/', '-', '//', '%', '**', 'r', 'b')
    if operator in tup_op:
        o = operation(input('X: '), input('Y: '))
        if o is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {o}')

    elif operator == 'sq':
        o = one_x(input('X: '))
        if o is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {o}')

    elif operator == 's':
        o = input('Enter the command add two numbers: ').split('+', 2)
        if '+' not in o:
            print('You entered the wrong characters!')
        op = operation((o[0]), (o[1]))
        if op is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {op}')

    elif operator == '^':
        o = input('Enter bitwise operation EXCLUSIVELY OR: ').split('^', 2)
        if '^' not in o:
            print('You entered the wrong characters!')
            continue
        op = operation((o[0]), (o[1]))
        if op is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {op}')

    elif operator == 'sqrt':
        o = input('Enter the square root of: ').split('sqrt', )
        op = one_x((o[0]))
        if op is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {op}')

        # Exit the program
    elif operator == 'x':
        print('Thank you, i hope you enjoyed working)')
        break

    else:
        print('You entered an incorrect character!!!')

