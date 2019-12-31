"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.
"""

import json


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def serialize(root):
    if not root:
        return None

    serialize_data = dict()
    serialize_left = serialize(root.left)
    serialize_right = serialize(root.right)

    serialize_data['data'] = root.val
    if serialize_left:
        serialize_data['left'] = serialize_left
    if serialize_right:
        serialize_data['right'] = serialize_right

    return json.dumps(serialize_data)


def deserialize(s):
    serialized_s = json.loads(s)

    node = Node(serialized_s['data'])
    if 'left' in serialized_s:
        node.left = deserialize(serialized_s['left'])
    if 'right' in serialized_s:
        node.right = deserialize(serialized_s['right'])

    return node


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

serialized_a = serialize(a)
print(serialized_a)

deserialized_a = deserialize(serialized_a)
assert str(deserialized_a) == "a"
