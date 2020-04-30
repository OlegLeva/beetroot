
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


def val_conv(item):
    '''validation and immediate conversion'''
    if item.replace(".", "", 1).isdigit():
        return float(item)
    return None

def operation(a, b):
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
    operator = input(f'please select the operation you need: ')
    operator = operator.replace(" ", "")
    tup_op = ('+', '*', '/', '-', '//', '%', '**', 'r', 'b')
    if operator in tup_op:
        o = operation(input('X: '), input('Y: '))
        if o is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {o}')

    # Exit the program
    elif operator == 'x':
        print('Thank you, i hope you enjoyed working)')
        break

    elif operator == 'sq':
        o = one_x(input('X: '))
        if o is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {o}')

    elif operator == 's':
        op = input('Enter the command add two numbers: ').split('+', 2)
        o = operation((op[0]), (op[1]))
        if o is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {o}')

    elif operator == '^':
        op = input('Enter bitwise operation EXCLUSIVELY OR: ').split('^', 2)
        o = operation((op[0]), (op[1]))
        if o is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {o}')
    elif operator == 'sqrt':
        op = input('Enter the square root of: ').split('sqrt', )
        o = one_x((op[0]))
        if o is None:
            print('You entered the wrong characters!')
            continue
        print(f'Result: {o}')

    else:
        print('You entered an incorrect character!!!')

