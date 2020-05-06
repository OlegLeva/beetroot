def opr():
    """ catch ValueError and ZeroDivisionError """
    try:
        a = input("Enter the number 'a': ")
        b = input("Enter the number 'b': ")
        z = (float(a) ** 2) / float(b)
        return z
    except ValueError:
        return 'You entered not a number!'
    except ZeroDivisionError:
        return 'Only stupid divide by zero'


print(opr())


def opr1():
    """ catch ValueError and ZeroDivisionError """
    try:
        a = input("Enter the number 'a': ")
        b = input("Enter the number 'b': ")
        z = (float(a) ** 2) / float(b)
        return z
    except (ValueError, ZeroDivisionError):
        return 'Something is entered incorrectly!'



print(opr1())