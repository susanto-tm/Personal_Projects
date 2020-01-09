"""
Solve expression trees
       *
    /    \
   +      +
 /  \   /   \
a   b   c   d

return (a + b) * (c + d)
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def evaluate_expressions(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return int(root.val)

    left_sum = evaluate_expressions(root.left)
    right_sum = evaluate_expressions(root.right)

    if root.val == "+":
        return left_sum + right_sum
    elif root.val == "-":
        return left_sum - right_sum
    elif root.val == "*":
        return left_sum * right_sum
    else:
        return left_sum / right_sum


def eval_exp(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return int(root.val)

    return eval("{} {} {}".format(eval_exp(root.left), root.val, eval_exp(root.right)))


a = Node("*")
b = Node("+")
c = Node("+")
d = Node("3")
e = Node("4")
f = Node("5")
g = Node("6")

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(eval_exp(a))