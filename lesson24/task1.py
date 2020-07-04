class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])


class StringReverser:
    def __init__(self):
        self.stack = Stack()

    def reverse_str(self, s):
        res = ""
        for i in range(len(s)):
            self.stack.push(s[i])

        while not self.stack.is_empty():
            res += self.stack.pop()

        return res


reverser = StringReverser()

print(reverser.reverse_str("HellO"))
