class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            last = self.head

            while last.next:
                last = last.next

            last.next = new_node

    def delete_node(self, ):
        pass