"""
Queue (FIFO First-In/First-Out)
"""


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def push(self, data):
        self.queue.append(data)

    def get(self):
        return self.queue.pop(0)


queue = Queue()
print(queue.is_empty())
queue.push(1)
queue.push(2)
queue.push(3)

print(queue.get())
print(queue.get())
print(queue.get())

