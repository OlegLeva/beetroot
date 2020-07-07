from sys import path

print(path)
print("_" * 50)
for j in path:
    print(j)

path.append("/Users/mymac/PycharmProjects/beetroot/lesson17/stack_list.py")
# C path можно работать как с обычным списком.
# Влияет на поиск, так как можно добавить path других модулей.
print("_" * 50)

for j in path:
    print(j)
print("_" * 50)

path.remove("/Users/mymac/PycharmProjects/beetroot")

for j in path:
    print(j)
