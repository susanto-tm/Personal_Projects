"""
Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_array(node, res):
    if node is None:
        return

    get_array(node.left, res)
    res.append(node.val)
    get_array(node.right, res)

    return res


def find_pairs(root, k):
    arr = get_array(root, [])

    for num in arr:
        if k - num in arr:
            return num, arr[arr.index(k-num)]

    return None


a = Node(10)
b = Node(5)
c = Node(15)
d = Node(11)
e = Node(15)

a.left = b
a.right = c
c.left = d
c.right = e

print(find_pairs(a, 20))

