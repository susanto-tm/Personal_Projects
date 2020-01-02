"""
Stack (LIFO Last-In/First-Out)
"""


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


stack = Stack()
stack.is_empty()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())
print(stack.pop())
print(stack.size())

