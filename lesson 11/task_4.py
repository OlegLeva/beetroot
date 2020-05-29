
class CustomException(Exception):

    def __init__(self, msg):
        x = open("logs.txt", "a+")
        x.write(msg + "\n")
        x.close()

    def __str__(self):
        return f'My exception: {"My CustomException"}'

    def __repr__(self):
        return f'My exception: {"My CustomException"}'
try:
    raise CustomException("My CustomException")
except CustomException as e:
    print(e)



