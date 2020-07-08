class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node:data={self.data}:next={self.next}>".format(self=self)

    @classmethod
    def fromList(cls, lst):
        """ Creates a linked list from normal python list """
        head = None

        while lst:
            s = lst.pop()
            node = Node(s)
            node.next = head
            head = node
        return head


#
# ["vasya"] -> ["puopkine"] -> ["cool"] -> ["man"]
#
#

# create a function that removes n-th element from linked list
# 1st element has number 0
def remove(head, n):
    if head is None:
        return head

    if n == 0:
        to_remove = head
        head = head.next
        del (to_remove)
        return head

    prev = head
    current = head.next
    current_number = 1

    # reach element n
    while current_number < n and current:
        prev = current
        current = current.next
        current_number += 1

    if current:  # if not the end of the list
        prev.next = current.next
        del (current)

    return head

# Homework
# - concatenate 2 linked lists
# - reverse a linked list
# - remove elements from m to n
# - remove elements by values
# - (*) create a doubly linked list from a linked list
