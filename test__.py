class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None



class SLinkedList:
    def __init__(self, e):
        self.headval = None
        self.e2 = None

    def __str__(self, ):
        return f"{self.e2}"

    def __repr__(self):
        return f"{self.e2}"

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
print(e2)