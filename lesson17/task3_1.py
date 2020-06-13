from lesson17_file.mymod import count_lines, count_chars, test
import sys

arg = sys.path[1:]
name = str(arg[0])

print(count_lines(name))
print(count_chars(name))
print(test(name))

