
import sys

sys.path.insert(0, "E:\beetroot\lesson17_file\mymod.py")

from lesson17_file import mymod

print(mymod.count_lines("text.txt"))
print(mymod.count_chars("text.txt"))
print(mymod.test("text.txt"))


