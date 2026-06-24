class myStack:
    def __init__(self, n):
        self.arr = []
        self.capacity = n

    def isEmpty(self):
        return len(self.arr) == 0

    def isFull(self):
        return len(self.arr) == self.capacity

    def push(self, x):
        if not self.isFull():
            self.arr.append(x)

    def pop(self):
        if not self.isEmpty():
            self.arr.pop()

    def peek(self):
        if self.isEmpty():
            return -1
        return self.arr[-1]