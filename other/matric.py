import random

n = 5
m = 7
r, t, y, x, c = random.randint(10,100), random.randint(10,100), random.randint(10,100), random.randint(10,100), random.randint(10,100)

a = [[r, t, y, x, c] for i in range(m)]
for i in a:

    print(i)