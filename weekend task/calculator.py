
# calculator with a question

name = input('Please enter your name: ')

name = name.replace(" ", "")
name = name.lower().title()

operation = input((f'{name}, Available operations:\n addition\n subtraction\n multiplication\ndivision\ndivision is complete'
                   f'\nremains of the number division\nraise the number to the degree\nround off the number'
                   f'\nfind the square of the number\nexit the program\nplease select the operation you need: '))


print(operation)