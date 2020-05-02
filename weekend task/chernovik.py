
# calculator with a question

name = input('Please enter your name: ')

# Brings a name to a normal format. Subject to suddenly a double name.
name = name.split()
name = ' '.join(name)
name = name.lower().title()

print(f'{name}, select an operation from the following list:\n'
                      f'Available operations:\naddition (+)\nsubtraction (-)\n'
                      f'multiplication (*)\ndivision (/)\ndivision is complete (//)'
                      f'\nremainder of division of numbers (%)\nraise the number to the degree (**)'
                      f'\nround off the number (r)\nfind the square of the number (sq)'
                      f'\nconverting from decimal to binary (b)\nthe command for adding two numbers (s)'
                      f'\nbitwise operation EXCLUSIVELY OR (^)\nsquare root of (sqrt)'
                      f'\nexit the program (x)')


def val_conv(s):
    """validation and immediate conversion"""
    s = s.strip()
    if not s:
        return
    # syntax check
    tmp = s
    if s[0] in "+-":
        tmp = s[1:]
    pieces = tmp.split(".")
    if len(pieces) > 2:
        return
    for p in pieces:
        if not p or not p.isdigit():
            return
    return float(s)


def operation(a, b):
    """mathematical operations with two data"""
    oper = operator
    x = val_conv(a)
    y = val_conv(b)

    if x is None or y is None:
        return None
    if oper == '+':
        return f'Addition: {float(x) + float(y)}'
    if oper == '*':
        return f'multiplication: {float(x) * float(y)}'
    if oper == '/':
        if y == 0:
            return 'cannot be divided by (0)'
        return f'division: {float(x) / float(y)}'
    if oper == '-':
        return f'subtraction: {float(x) - float(y)}'
    if oper == '//':
        if y == 0:
            return 'cannot be divided by (0)'
        return f'division is complete: {float(x) // float(y)}'
    if oper == '%':
        if y == 0:
            return 'cannot be divided by (0)'
        return f'remainder of division of numbers: {float(x) % float(y)}'
    if oper == '**':
        return f'raise the number to the degree: {float(x) ** float(y)}'
    if oper == 'r':
        return f'round off the number: {round(float(x), int(y))}'
    if oper == 'b':
        return f'Decimal converted to binary: {bin(int(x))}'
    if oper == 's':
        return f'the sum of two numbers:  {int(x) + int(y)}'
    if oper == '^':
        return f'bitwise operation EXCLUSIVELY OR:  {int(x) ^ int(y)}'

def one_x(a):
    """mathematical operations with one input"""
    oper = operator
    x = val_conv(a)
    if x is None:
        return None
    if oper == 'sq':
        return f'The square root of the number is: {float(x) **(1/2)}'
    if oper == 'sqrt':
        from math import sqrt
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

    if operator == 'sq':
        o = one_x(input('X: '))
        if o is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {o}')

    if operator == 's':
        o = input('Enter the command add two numbers: ').split('+', 2)
        if '+' not in o:
            print('You entered the wrong characters!')
        op = operation((o[0]), (o[1]))
        if op is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {op}')

    if operator == '^':
        o = input('Enter bitwise operation EXCLUSIVELY OR: ').split('^', 2)
        if '^' not in o:
            print('You entered the wrong characters!')
            continue
        op = operation((o[0]), (o[1]))
        if op is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {op}')

    if operator == 'sqrt':
        o = input('Enter the square root of: ').split('sqrt', )
        if "-" in o:
            print('For real numbers, the root of the negative number does not exist')
            continue
        op = one_x((o[0]))
        if op is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {op}')

        # Exit the program
    if operator == 'x':
        print('Thank you, i hope you enjoyed working)')
        break

    else:
        print('You entered an incorrect character!!!')

import