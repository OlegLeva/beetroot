# Поки не вийшло

import random
l1 = [random.randint(0,10) for r in range(10)]
l2 = [random.randint(0,10) for t in range(10)]
res = []
i, j, n, = 0, 0, 0

while i < len(l1) and j < len(l2):
    if l1[i] == l2[j]:
        res.append(l1[i])
        i += 1
    else:
        pass
        j += 1
print(l1)
print(l2)
print(res)

