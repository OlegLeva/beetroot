# Дибільний спосіб получився(( (відсортував, та вивів останній)

import random

l = [random.randint(0, 100) for i in range(10)]

# 1 way
print(max(l))

# 2 way
n = len(l)
i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
        j += 1
    i += 1

print(l[-1])

# 3 way
l = sorted(l)
print(l[-1])

