from lesson17_file.mymod import count_lines, count_chars, test
import sys

sys.path.insert(1, "/Users/mymac/PycharmProjects/beetroot/lesson17_file/mymod.py")
# не хочет работать, или я не умею обращаться с терминалом(((
#Думаю что PYTHONPATH включать каталог нужно, что бы можно было к нему обращаться по индексу.


print(count_lines("text.txt"))
print(count_chars("text.txt"))
print(test("text.txt"))

#Наблюдаются постоянные проблемы неумения работы с терминалом(((
