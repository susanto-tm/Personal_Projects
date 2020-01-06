"""
Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right,
and satisfies the constraint that the key in the left child must be less than or equal to the root
and the key in the right child must be greater than or equal to the root.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(node, output):
    if node is None:
        return

    inorder_traversal(node.left, output)
    output.append(node.val)
    inorder_traversal(node.right, output)


def is_valid(node):
    output = []
    inorder_traversal(node, output)

    for i in range(len(output) - 1):
        if output[i+1] < output[i]:
            return False

    return True


a = Node(3)
b = Node(1)
c = Node(4)

a.left = b
a.right = c

print(is_valid(a))
