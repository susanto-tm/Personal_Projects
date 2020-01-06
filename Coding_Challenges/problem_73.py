"""
Given the head of a singly linked list, reverse it in-place.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def reverse_iter(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def reverse_recur(self, curr, prev):
        if curr.next is None:
            self.head = curr

            curr.next = prev
            return

        next_node = curr.next

        curr.next = prev

        self.reverse_recur(next_node, curr)

    def print_val(self):
        head = self.head

        while head:
            print(str(head.val) + "->", end="")
            head = head.next


lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.print_val()
print()
lst.reverse_iter()
lst.print_val()

print()
lst2 = LinkedList()
lst2.append(1)
lst2.append(2)
lst2.append(3)
lst2.append(4)

lst2.print_val()
print()
lst2.reverse_recur(lst2.head, None)
lst2.print_val()
