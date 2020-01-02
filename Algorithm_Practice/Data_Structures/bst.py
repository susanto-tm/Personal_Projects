"""
Balanced Binary Search Tree
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_bst(arr):
    if not arr:
        return None

    mid = len(arr) // 2

    root = Node(arr[mid])

    root.left = build_bst(arr[:mid])
    root.right = build_bst(arr[mid+1:])

    return root


def pre_order(node):
    if not node:
        return

    print(node.val, end=" ")
    pre_order(node.left)
    pre_order(node.right)


lst = [1, 2, 3, 5, 6, 10]
node_a = build_bst(lst)
pre_order(node_a)

