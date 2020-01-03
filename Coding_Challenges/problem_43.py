"""
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack

pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack,
then it should throw an error or return null.

max(), which returns the maximum value in the stack currently. If there are no elements in the stack,
then it should throw an error or return null.

Each method should run in constant time.
"""


class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.max_stack or val > self.max_stack[-1]:
            self.max_stack.append(len(self.stack) - 1)  # append index of maximum value

    def pop(self):
        if not self.stack:
            return None

        if len(self.stack) - 1 == self.max_stack[-1]:
            self.max_stack.pop()

        return self.stack.pop()

    def max(self):
        if not self.stack:
            return None

        return self.stack[self.max_stack[-1]]


s = Stack()
s.push(1)
s.push(3)
s.push(5)
s.push(4)
s.push(6)

assert s.max() == 6
assert s.pop() == 6
