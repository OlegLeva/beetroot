
def with_index(iterable, start=0):
    result = []
    while start < len(iterable):
        l = (start, iterable[start])
        result.append(l)
        start += 1
    return result

print(with_index([6, 7, 2, 9]))


def with_index_1(iterable_1, start_1=0):
    while start_1 < len(iterable_1):
        yield (start_1, iterable_1[start_1])
        start_1 += 1


print(list(with_index_1([6, 7, 't', 9])))