
def opr():
    """ catch ValueError and ZeroDivisionError """
    try:
        a = input("Enter the number 'a': ")
        b = input("Enter the number 'b': ")
        z = (float(a) ** 2) / float(b)
        return z

    except:
        return 'Only stupid divide by zero'
print(opr())