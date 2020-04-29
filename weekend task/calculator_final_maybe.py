
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

def one_x(a):
    x = val_conv(a)
    if operator == 'sq':
        if x is None:
            return None
        return x **(1/2)



while True:
    operator = None
    # Exit the program
    if operator == 'x':
        print('Thank you, i hope you enjoyed working)')
        break

    while True:
        operator = input(f'please select the operation you need: ')
        operator = operator.replace(" ", "")
        #if operator == '+' or '*' or '/' or '-' or '//' or '%' or '**' or 'r':
            o = operation(input('X: '), input('Y: '))
            if o is None:
                print('You entered the wrong characters!')
                continue
            print(f'Result: {o}')
            break
        elif operator == 'sq':
            o = one_x(input('X: '))
            if o is None:
                print('You entered the wrong characters!')
                continue
            print(f'Result: {o}')
            break


        else:
            print('You entered an incorrect character!!!')


#operator in ('//', '**', '+', '')

#operator == "/" or operator == "-"