"""
Given a binary tree and an integer k, return whether there exists a root-to-leaf path that sums up to k.

For example, given k = 18 and the following binary tree:

    8
   / \
  4   13
 / \   \
2   6   19
Return True since the path 8 -> 4 -> 6 sums to 18.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def has_path(node, s):
    if node is None:
        return s == 0

    else:
        ans = 0
        sub_sum = s - node.val

        if sub_sum == 0 and node.left is None and node.right is None:
            return True

        if node.left is not None:
            ans = has_path(node.left, sub_sum) if has_path(node.left, sub_sum) else ans
        if node.right is not None:
            ans = has_path(node.right, sub_sum) if has_path(node.right, sub_sum) else ans

        return ans


a = Node(8)
b = Node(4)
c = Node(13)
d = Node(2)
e = Node(6)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

k = 18
print(has_path(a, k))
