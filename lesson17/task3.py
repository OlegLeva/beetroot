from lesson17_file.mymod import count_lines, count_chars, test
import sys

sys.path.insert(1, "/Users/mymac/PycharmProjects/beetroot/lesson17_file/mymod.py")


print(count_lines("text.txt"))
print(count_chars("text.txt"))
print(test("text.txt"))

#Наблюдаются постоянные проблемы работы с терминалом(((