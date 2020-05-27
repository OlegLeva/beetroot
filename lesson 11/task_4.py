
class CustomException(Exception):

    def __init__(self, msg):
        x = open(" logs.txt", "a+")
        x.write(msg + "\n")
        x.close()

    def __str__(self):
        return 'My exception'

    def __repr__(self):
        return 'My exception'
try:
    raise CustomException ("My CustomException")
except CustomException as e:
    print(e)



