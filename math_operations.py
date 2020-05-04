def operation(x, y):
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
    return oper[]
