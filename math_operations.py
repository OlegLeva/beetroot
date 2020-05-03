def operation(x, y): #добавить потом х = val_conv(a) и у = val_conv(b)
    """mathematical operations with two data"""

    from perf1_operat import add, mult, div, sub, divb, divby, deg, addauto, bit
    oper = {'+': add(x, y),
            '*': mult(x, y),
            '/': div(x, y),
            '-': sub(x, y),
            '//': divb(x, y),
            '%': divby(x, y),
            '**': deg(x, y),
            'r': round(x, y),
            'b': bin(x),
            's': addauto(x, y),
            '^': bit(x, y)
            }

    if x is None or y is None:
        return None
    if oper == '+':
        add(x,y)
    if oper == '*':
        return f'multiplication: {float(x) * float(y)}'
    if oper == '/':
        if y == 0:
            return 'cannot be divided by (0)'
        return f'division: {float(x) / float(y)}'
    if oper == '-':
        return f'subtraction: {float(x) - float(y)}'
    if oper == '//':
        if y == 0:
            return 'cannot be divided by (0)'
        return f'division is complete: {float(x) // float(y)}'
    if oper == '%':
        if y == 0:
            return 'cannot be divided by (0)'
        return f'remainder of division of numbers: {float(x) % float(y)}'
    if oper == '**':
        return f'raise the number to the degree: {float(x) ** float(y)}'
    if oper == 'r':
        return f'round off the number: {round(float(x), int(y))}'
    if oper == 'b':
        return f'Decimal converted to binary: {bin(int(x))}'
    if oper == 's':
        return f'the sum of two numbers:  {int(x) + int(y)}'
    if oper == '^':
        return f'bitwise operation EXCLUSIVELY OR:  {int(x) ^ int(y)}'
