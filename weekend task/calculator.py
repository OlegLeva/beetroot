
# calculator with a question

name = input('Please enter your name: ')

#name = name.replace(" ", "") Хотел сразу так реализовать (но вдруг двойное имя типа "Аве Мария"))


name = name.split()
name = ' '.join(name)
name = name.lower().title()

operator = None

while operator != 'x':

    operator = input((f'{name}, select an operation from the following list:\n'
                      f'Available operations:\naddition (+)\nsubtraction (-)\n'
                      f'multiplication (*)\ndivision (/)\ndivision is complete (//)'
                      f'\nremainder of division of numbers (%)\nraise the number to the degree (**)'
                      f'\nround off the number (r)\nfind the square of the number (sq)'
                      f'\nconverting from decimal to binary (b)\nexit the program (x)'
                      f'\nplease select the operation you need: '))

    if operator == '+':
    # Addition
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        print(f'Addition of numbers is equal to: {x + y}')
    # subtracting
    elif operator == '-':
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        print(f'subtracting two numbers is equal to: {x - y}')
    # Multiplying
    elif operator == '*':
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        print(f'Multiplying two numbers equals: {x * y}')
    # Division
    elif operator == '/':
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        print(f'Divisioning two numbers equals: {x / y}')
    # The integer division
    elif operator == '//':
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        print(f'The integer division of two numbers is equal to: {x // y}')
    # Remainder of division of two numbers
    elif operator == '%':
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        print(f'Remainder of division of two numbers is equal to: {x % y}')
    # Raise the number to a degree
    elif operator == '**':
        x = float(input('Enter the number: '))
        y = float(input('Enter the degree number: '))
        print(f'The number in degree is: {x ** y}')
    # Rounding the first number to n decimal places (when entering n - the second number)
    elif operator == 'r':
        x = float(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        print(f"rounding the first number to 'n' decimal places (where 'n' is the second number): {round(x,y)}")
    # Find the square of the number
    elif operator == 'sq':
        x = float(input('Enter the number: '))
        print(f'The square root of the number is: {x **(1/2)}')
    # Converting from decimal to binary
    elif operator == 'b':
        x = int(input('Enter the number: '))
        print(f'Decimal converted to binary: {bin(x)}')

    # Exit the program
    elif operator == 'x':
        print('Thank you, i hope you enjoyed working)')
        break

    else:
        print('You entered an incorrect character!!!')