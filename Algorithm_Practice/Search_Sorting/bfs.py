class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.head = None

    def __str__(self):
        last = self.head
        while last:
            print(last.val, end=' ')
            last = last.next

    __repr__ = __str__

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def dequeue(self):
        curr = self.head
        self.head = self.head.next
        return curr.val

    def __len__(self):
        count = 0
        last = self.head
        while last:
            count += 1
            last = last.next

        return count

    def isEmpty(self):
        return self.head is None



class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if node is None:
            self.root = Node(data)
        else:
            if data < node.val:
                if node.left is None:
                    node.left = Node(data)
                else:
                    self.insert(node.left, data)
            else:
                if node.right is None:
                    node.right = Node(data)
                else:
                    self.insert(node.right, data)

    @property
    def getMin(self):
        if self.root is None:
            return None

        node = self.root
        while node.left:
            node = node.left

        return node.val

    def bfs(self):
        queue = Queue()
        if self.root is None:
            return None

        queue.enqueue(self.root)
        nodes = []

        while not queue.isEmpty():
            node = queue.dequeue()
            nodes.append(node.val)

            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)

        return nodes


x=BinarySearchTree()
x.insert(x.root,9)
x.insert(x.root,4)
x.insert(x.root,11)
x.insert(x.root,2)
x.insert(x.root,5)
x.insert(x.root,10)
x.insert(x.root,9.5)
x.insert(x.root,7)