"""
Singly Linked Lists
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        # if head is empty or new list
        if self.head is None:
            self.head = new_node
            return

        # else move current list back
        prev_head = self.head
        self.head = new_node
        self.head.next = prev_head

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def append_after(self, mid, data):
        head = self.head

        while head:
            if head.val == mid:
                break
            head = head.next

        if head is None:
            print("Node does not exist")
            return

        new_node = Node(data)
        new_node.next = head.next
        head.next = new_node

    def remove(self, remove_node):
        head = self.head
        prev = None

        if head is not None:
            if head.val == remove_node:
                self.head = head.next
                return

        while head is not None:
            if head.val == remove_node:
                break
            prev = head
            head = head.next

        if head is None:
            return

        prev.next = head.next

    def print_val(self):
        head = self.head

        while head:
            print(str(head.val) + "->", end="")
            head = head.next

        if head is None:
            print("NULL", end="")


lst = LinkedList()
lst.head = Node(10)
lst.append(12)
lst.append(15)
lst.append(0)
lst.push(30)
lst.append_after(12, 100)
lst.print_val()
