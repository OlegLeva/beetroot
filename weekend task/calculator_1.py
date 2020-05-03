from check_namemenu import menu
from check_operator import input_operator

name = input('Please enter your name: ')

print(menu(name))

operator = input(f'please select the operation you need: ')
operator = operator.replace(" ", "")

print(input_operator(operator))

