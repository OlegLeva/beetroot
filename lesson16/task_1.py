#
# def with_index(iterable, start=0):
#     result = []
#     while start < len(iterable):
#         l = (start, iterable[start])
#         result.append(l)
#         start += 1
#     return result
#
# print(with_index([6, 7, 2, 9]))


def with_index_1(iterable_1, start_1=0):
    if start_1 >= len(list(iterable_1)):
        raise StopIteration
    for i in iterable_1:
        yield (start_1, i)
        start_1 += 1


def gen():
    for j in [6, 7, 8, 9]:
        yield j

generator = gen()
g = with_index_1(generator)
print(next(g))
print(next(g))

