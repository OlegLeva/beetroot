from sys import path

print(path)
print("_"*50)
for j in path:
    print(j)

path.append("/Users/mymac/PycharmProjects/beetroot/lesson17/task1_1.py")
#C path можно работать как с обычным списком.
#Влияет на поиск, так как можно добавить path других модулей. Но что-то мне подсказывает, что так делать не нужно)))
print("_"*50)

for j in path:
    print(j)
print("_"*50)

path.remove("/Users/mymac/PycharmProjects/beetroot")

for j in path:
    print(j)
