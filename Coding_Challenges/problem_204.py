"""
Given a complete binary tree, count the number of nodes in faster than O(n) time.
Recall that a complete binary tree has every level filled except the last,
and the nodes in the last level are filled starting from the left.
"""


class Node:
    def __init__(self):
        self.left = None
        self.right = None


def count_nodes(root, left=0, right=0):
    if not root:
        return

    if not left:
        node = root
        while node:
            node = node.left
            left += 1

    if not right:
        node = root
        while node:
            node = node.right
            right += 1

    if left == right:
        return 2**left - 1  # 2 ^ x subtracted by second level right side

    return 1 + count_nodes(root.left, left=left-1, right=right-1) + count_nodes(root.right, left=left-1, right=right-1)


a = Node()
b = Node()
c = Node()
d = Node()
e = Node()
f = Node()
g = Node()

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(count_nodes(a))
