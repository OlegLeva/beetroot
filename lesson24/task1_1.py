class Stack(list):
    push = list.append

    def is_empty(self):
        return not self


class StringReverser:
    def __init__(self):
        self.stack = Stack()

    def reverse_str(self, s):
        res = ""
        for i in range(len(s)):
            self.stack.push(s[i])

        while self.stack:
            res += self.stack.pop()

        return res


reverser = StringReverser()

print(reverser.reverse_str("HellO"))