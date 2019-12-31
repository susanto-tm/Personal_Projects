"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print_list(self):
        head = self.head

        while head:
            print(str(head.val) + "->", end="")
            head = head.next


A = LinkedList()
A.append(3)
A.append(7)
A.append(8)
A.append(10)

B = LinkedList()
B.append(99)
B.append(1)
B.append(8)
B.append(10)


def intersecting_node(l1, l2):
    l1_lst = []

    head = l1.head
    while head:
        l1_lst.append(head.val)
        head = head.next

    head = l2.head
    while head:
        if head.val in l1_lst:
            return head.val
        head = head.next

    return None


print(intersecting_node(A, B))

