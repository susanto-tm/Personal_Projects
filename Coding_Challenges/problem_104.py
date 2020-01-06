"""
Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns true while 1 -> 4 returns false.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


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
        new_node.prev = last

    def palindrome_doubly(self):
        output = []
        prev = None
        node = self.head

        while node:
            output.append(node.val)
            prev = node
            node = node.next

        for data in output:
            if prev.val != data:
                return False
            prev = prev.prev

        return True

    def palindrome_singly(self):
        output = []
        node = self.head

        while node:
            output.append(node.val)
            node = node.next

        return output == output[::-1]

    def print_val(self):
        head = self.head

        while head:
            print(str(head.val) + "->", end="")
            head = head.next


lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(2)
print(lst.palindrome_singly())

