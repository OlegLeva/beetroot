def input_operator(operator):

    while True:
        '''input processing'''

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

