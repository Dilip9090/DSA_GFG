class myQueue:
    def __init__(self, n):
        self.arr = []
        self.capacity = n

    def isEmpty(self):
        return len(self.arr) == 0

    def isFull(self):
        return len(self.arr) == self.capacity

    def enqueue(self, x):
        if not self.isFull():
            self.arr.append(x)

    def dequeue(self):
        if not self.isEmpty():
            self.arr.pop(0)

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr[0]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.arr[-1]