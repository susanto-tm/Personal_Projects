"""
Given the root to a binary search tree, find the second largest node in the tree.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_largest_parent(node):
    parent = None
    while node.right:
        parent = node
        node = node.right

    return node, parent


def find_second_largest(root):
    if not root:
        return None

    if root.left and not root.right:
        second_largest, _ = find_largest_parent(root.left)  # since root.left < root: last node of root.right is 2nd
    else:
        _, second_largest = find_largest_parent(root)  # check node.right until end and parent is 2nd

    print("Second largest", second_largest.val)

    return second_largest


def test0():
    node_a = Node(5)
    node_b = Node(3)
    node_c = Node(8)
    node_d = Node(2)
    node_e = Node(4)
    node_f = Node(7)
    node_g = Node(9)
    node_a.left = node_b
    node_a.right = node_c
    node_b.left = node_d
    node_b.right = node_e
    node_c.left = node_f
    node_c.right = node_g

    assert find_second_largest(node_a).val == 8
