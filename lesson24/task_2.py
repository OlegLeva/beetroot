# Захотелось реализовать без класса.


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
print(check_balanced("((())"))


