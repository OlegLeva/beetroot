
# the valid phone number program

x = input('Enter phone number: ')
if x.isdigit() and len(x) == 10:
    print('Your phone number: ', x)
else:
    print('Incorrect phone number')
