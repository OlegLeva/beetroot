
#String manipulation

s1 = input("Please enter 'helloworld': ")
s1 = s1.strip(' ')
print(s1[:2] + s1[-2:])

s2 = input("Please enter 'my': ")
s2 = s2.strip(' ')
print(s2*2)

s3 = input("Please enter'x': ")
s3 = s3.strip(' ')
if len('x') < 2:
    print('')
