
def in_range(start=0, end=None, step=1):
    if type(start) != int or type(end) != int or type(step) != int:
        raise TypeError('enter the number')
    result = []
    while start != end:
        result.append(start)
        start += step
    return result


print(in_range(1, 6))


def in_range1(start1=0, end1=None, step1=1):
    if type(start1) != int or type(end1) != int or type(step1) != int:
        raise TypeError('enter the number')
    while start1 != end1:
        yield start1
        start1 += step1


print(list(in_range1(1, 6)))
print(list(in_range1(0, 50, 5)))



