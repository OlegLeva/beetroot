
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
                      f'\nbitwise operation EXCLUSIVELY OR (^)'
                      f'\nexit the program (x)')

operator = None

while True:

    operator = input(f'please select the operation you need: ')
    # Remove extra spaces
    operator = operator.replace(" ", "")

    if operator == '+':
    # Addition
        x = input('Enter the first number: ')
        x = x.replace(" ", "")
        y = input('Enter the second number: ')
        y = y.replace(" ", "")
        print(f'Addition of numbers is equal to: {float(x) + float(y)}')
    # subtracting
    elif operator == '-':
        x = input('Enter the first number: ')
        x = x.replace(" ", "")
        y = input('Enter the second number: ')
        y = y.replace(" ", "")
        print(f'subtracting two numbers is equal to: {float(x) - float(y)}')
    # Multiplying
    elif operator == '*':
        x = input('Enter the first number: ')
        x = x.replace(" ", "")
        y = input('Enter the second number: ')
        y = y.replace(" ", "")
        print(f'Multiplying two numbers equals: {float(x) * float(y)}')
    # Division
    elif operator == '/':
        x = input('Enter the first number: ')
        x = x.replace(" ", "")
        y = input('Enter the second number: ')
        y = y.replace(" ", "")
        print(f'Divisioning two numbers equals: {float(x) / float(y)}')
    # The integer division
    elif operator == '//':
        x = input('Enter the first number: ')
        x = x.replace(" ", "")
        y = input('Enter the second number: ')
        y = y.replace(" ", "")
        print(f'The integer division of two numbers is equal to: {float(x) // float(y)}')
    # Remainder of division of two numbers
    elif operator == '%':
        x = input('Enter the first number: ')
        x = x.replace(" ", "")
        y = input('Enter the second number: ')
        y = y.replace(" ", "")
        print(f'Remainder of division of two numbers is equal to: {float(x) % float(y)}')
    # Raise the number to a degree
    elif operator == '**':
        x = input('Enter the number: ')
        x = x.replace(" ", "")
        y = input('Enter the degree number: ')
        y = y.replace(" ", "")
        print(f'The number in degree is: {float(x) ** float(y)}')
    # Rounding the first number to n decimal places (when entering n - the second number)
    elif operator == 'r':
        x = input('Enter the first number: ')
        x = x.replace(" ", "")
        y = input('Enter the second number: ')
        y = y.replace(" ", "")
        print(f"rounding the first number to 'n' decimal places (where 'n' is the second number): {round(float (x),int(y))}")
    # Find the square of the number
    elif operator == 'sq':
        x = input('Enter the number: ')
        x = x.replace(" ", "")
        print(f'The square root of the number is: {float(x) **(1/2)}')
    # Converting from decimal to binary
    elif operator == 'b':
        x = input('Enter the number: ')
        x = x.replace(" ", "")
        print(f'Decimal converted to binary: {bin(int(x))}')
    # The command for adding two numbers:
    elif operator == 's':
        op = input('Enter the command add two numbers: ').split('+', 2)
        print(int(op[0]) + int(op[1]))
    # Bitwise operation EXCLUSIVELY OR
    elif operator == '^':
        op = input('Enter bitwise operation EXCLUSIVELY OR: ').split('^', 2)
        print(int(op[0]) ^ int(op[1]))
    # The square root of number command
    elif operator == 'sqrt':
        import math
        op = input('Enter the square root of: ').split('sqrt', )
        x = int(op[1])
        print(math.sqrt(x))

    # Exit the program
    elif operator == 'x':
        print('Thank you, i hope you enjoyed working)')
        break

    else:
        print('You entered an incorrect character!!!')




