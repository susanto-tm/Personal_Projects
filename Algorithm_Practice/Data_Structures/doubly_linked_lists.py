"""
Doubly Linked Lists
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        prev_head = self.head
        self.head = new_node
        self.head.next = prev_head
        prev_head.prev = self.head

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

    def append_after(self, after_node, data):
        head = self.head

        while head:
            if head.val == after_node:
                break
            head = head.next

        if head is None:
            print("Node does not exist")
            return

        new_node = Node(data)
        mid_next = head.next

        head.next = new_node
        new_node.prev = head

        new_node.next = mid_next
        mid_next.prev = new_node

    def remove(self, data):
        if self.head is None:
            print("List does not exist")
            return

        prev = None
        head = self.head

        while head:
            if head.val == data:
                break
            prev = head
            head = head.next

        if head is None:
            return

        new_next = head.next
        prev.next = new_next
        new_next.prev = prev

    def print_val(self):
        head = self.head

        while head:
            print(str(head.val) + "-><-", end="")
            head = head.next

        if head is None:
            print("NULL", end="")


lst = LinkedList()
lst.append(10)
lst.push(13)
lst.append(11)
lst.append_after(10, 30)
lst.print_val()
