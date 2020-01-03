"""
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure
with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
"""


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, val):
        self.stack1.append(val)

    def dequeue(self):
        s1 = self.stack1
        s2 = self.stack2

        if not s1:
            return None

        while s1:
            s2.append(s1.pop())
        val = s2.pop()
        while s2:
            s1.append(s2.pop())
        return val


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

assert q.dequeue() == 1
assert q.dequeue() == 2
assert q.dequeue() == 3
assert not q.dequeue()
