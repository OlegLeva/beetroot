def one_x(a):
    """mathematical operations with one input"""
    oper = operator
    x = val_conv(a)
    if x is None:
        return None
    if oper == 'sq':
        return f'The square root of the number is: {float(x) **(1/2)}'
    if oper == 'sqrt':
        from math import sqrt
        return (f'square root: {sqrt(x)}')
    