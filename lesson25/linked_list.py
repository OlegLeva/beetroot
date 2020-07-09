class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = 0

    def __repr__(self):
        return f"{self.data}"

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False



class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        print_data = self.head
        while print_data is not None:
            print(print_data.data)
            print_data = print_data.next

    def __repr__(self):
        return f"{self.head}"

my_list = LinkedList()
my_list.head = Node("Vasya")
elem = Node("Petya")
elem2 = Node("Kolya")
my_list.head.next = elem
elem.next = elem2
elem3 = Node("Marta")
elem2.next = elem3


print(my_list)
print(my_list.head.next.next)
print(elem.next.next)

print(Node.has_value(elem2.next, "Marta"))

my_list.listprint()

