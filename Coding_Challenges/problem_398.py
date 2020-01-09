"""
Given a linked list and an integer k, remove the k-th node from the end of the list and return the head of the list
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def remove_node(self, k):
        first = self.head
        second = self.head
        count = 0

        while count < k:
            second = second.next
            count += 1

        if second is None:
            return self.head
        elif second.next is None:
            self.head = self.head.next
            return self.head

        while second.next:
            first = first.next
            second = second.next

        first.next = first.next.next
        return self.head

    def print_val(self):
        head = self.head

        while head:
            print(str(head.val) + "->", end="")
            head = head.next

        print()


lst = LinkedList()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in arr:
    lst.create(i)

lst.print_val()
lst.remove_node(8)
lst.print_val()
