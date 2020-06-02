def is_isogram(string):
    x = set(string)
    if len(x) == len(string):
        return True
    elif len(x) != len(string):
        return False
print(is_isogram("Rom"))




