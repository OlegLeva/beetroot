
# calculator with a question

name = input('Please enter your name: ')

# Brings a name to a normal format. Subject to suddenly a double name.
import check_namemenu
check_namemenu.menu(name)

# syntax check
from val_conv5 import val_conv


#from math_operations import operation

def operation1(a):
    """mathematical operations with two data"""
    x = val_conv(a)
    if x is None:
        return None
    from perf1_operat import sq1, bin
    oper1 = {
            'sq': sq1(x),
            'b': bin(int(x)),
            }
    return oper1[operator]


def operation(a, b):
    """mathematical operations with two data"""
    x = val_conv(a)
    y = val_conv(b)
    if x is None or y is None:
        return None
    from perf1_operat import add, mult, div, sub, divb, divby, deg, addauto, bit, round
    oper = {
            '+': add(x, y),
            '*': mult(x, y),
            '/': div(x, y),
            '-': sub(x, y),
            '//': divb(x, y),
            '%': divby(x, y),
            '**': deg(x, y),
            'r': round(int(x), int(y)),
            's': addauto(x, y),
            '^': bit(x, y),
            }
    return oper[operator]

while True:
    '''input processing'''
    operator = input(f'please select the operation you need: ')
    operator = operator.replace(" ", "")
    tup_op1 = ('+', '*', '/', '-', '//', '%', '**', 'r', 'b', '^', )
    if operator in tup_op1:
        o = operation(input('X: '), input('Y: '))
        if o is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {o}')

    tup_op2 = ('sq')
    if operator in tup_op2:
        o = operation1(input('X: '))
        if o is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {o}')
    # Exit the program
    if operator == 'x':
        print('Thank you, i hope you enjoyed working)')
        break

    if operator not in tup_op1:
        print('You entered an incorrect character!!!')
        continue
    elif operator not in tup_op2:
        print('You entered an Incorrect character!!!')
        continue





