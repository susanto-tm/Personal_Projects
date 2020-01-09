"""
Given a linked list of numbers and a pivot `k`, partition the linked list so that all nodes less than `k`
come before nodes greater than or equal to `k`.

For example, given the linked list `5 -> 1 -> 8 -> 0 -> 3` and `k = 3`, the solution could be `1 -> 0 -> 5 -> 8 -> 3`.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next  = None


def get_nodes(arr):
    next_node = None
    for value in arr[::-1]:
        node = Node(value)
        node.next = next_node
        next_node = node

    return next_node  # since reversed becomes head


def get_list(head):
    node = head
    nodes = list()
    while node:
        nodes.append(node.val)
        node = node.next

    return nodes


def partition(llist, k):
    head = llist
    prev, curr = head, head.next

    while curr:
        if curr.val < k:
            prev.next = curr.next
            curr.next = head
            head = curr  # head keeps track of smallest and changes smaller to head
            curr = prev.next
        else:
            prev = curr
            curr = curr.next

    return head


print(get_list(partition(get_nodes([5, 1, 8, 0, 3]), 3)))
