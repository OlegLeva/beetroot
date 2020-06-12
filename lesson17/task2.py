import task1_1
from sys import path
"""Список менять можно
   На поиск не влияет"""

print(path)
for j in path:
    print(j)
print()
path.pop(0)
path.clear()

print(path)

print(task1_1.sq(3))

