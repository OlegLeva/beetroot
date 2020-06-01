a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

def sort_str(a, b):
    return "".join(sorted(set(a + b)))

print(sort_str(a, b))


def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i * i
    return sum


print(square_sum([1, 2, 2]))


