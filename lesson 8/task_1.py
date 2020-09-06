def oops():
    raise IndexError


def catch():
    try:
        oops()
    except IndexError:
        return 'IndexError caught'


print(catch())


###############################


def oops1():
    t = (5, 4, 4, 7, 8)
    return t[8]


def catch1(z):
    return z


try:
    catch1(oops1())
except IndexError:
    print('IndexError caught')

#################################
'''

def oops2():
    raise KeyError

def catch2(y):
    return y

try:
    catch2(oops2())
except IndexError:
    print('IndexError caught')
'''
#################################

"""def oops3():
    q = {'J': 2, 'p': 3}
    return q['m']

def catch3(k):
    return k

try:
    catch3(oops3())
except IndexError:
    print('IndexError caught')"""
