"""
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer
and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def solve_graph(root):
    if root.val.isnumeric():
        return float(root.val)

    return eval("{} {} {}".format(solve_graph(root.left), root.val, solve_graph(root.right)))


node_a = Node("*")
node_b = Node("+")
node_c = Node("3")
node_d = Node("2")
node_e = Node("+")
node_f = Node("4")
node_g = Node("5")

node_a.left = node_b
node_b.left = node_c
node_b.right = node_d
node_a.right = node_e
node_e.left = node_f
node_e.right = node_g

print(solve_graph(node_a))
print(solve_graph(node_e))
