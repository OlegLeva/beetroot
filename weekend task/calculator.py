
# calculator with a question

name = input('Please enter your name: ')

name = name.replace(" ", "")
name = name.lower().title()

operator = None


while operator != 'x':

    operator = input((f'{name}, select an operation from the following list:\n'
                      f'Available operations:\naddition (+)\nsubtraction (-)\n'
                      f'multiplication (*)\ndivision (/)\ndivision is complete (//)'
                      f'\nremainder of division of numbers (%)\nraise the number to the degree (**)'
                      f'\nround off the number\nfind the square of the number'
                      f'\nexit the program (x)\nplease select the operation you need: '))

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

    # rounding the first number to 'n' decimal places (where 'n' is the second number)
    elif operator == 'r':
        x = float(input('Enter the first number: '))
        z = int(input('Enter the second number: '))
        print(f"rounding the first number to 'n' decimal places (where 'n' is the second number): {round(x.z)}")


    elif operator == 'x':
        print('Thank you, i hope you enjoyed working)')
        break

    else:
        print('You entered an incorrect character!!!')