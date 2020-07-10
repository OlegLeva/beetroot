# Захотелось реализовать без класса.

'''
def check_balanced(items):
    stack = []
    for item in items:
        if item == "(":
            stack.append(item)
        if item == ")":
            if stack == []:
                return False
            if stack != []:
                stack.pop()
    if stack == []:
        return True
    else:
        return False

print(check_balanced("((()))"))
print(check_balanced("(()))"))
print(check_balanced("((())"))'''


def check_balanced(items):
    stack = []
    for item in items:
        if item == "(" or item == "[" or item == "{":
            stack.append(item)
        elif item == ")" or item == "]" or item == "}":
            if stack == []:
                return False
            elem = stack.pop()
            if not comparison(elem, item):
                return False

    if stack != []:
        return False
    else:
        return True


def comparison(opening, closing):
    if opening == "(" and closing == ")":
        return True
    if opening == "[" and closing == "]":
        return True
    if opening == "{" and closing == "}":
        return True
    return False


print(check_balanced("([]([({})]){})"))
print(check_balanced("(({(])}))"))
print(check_balanced("((())"))
