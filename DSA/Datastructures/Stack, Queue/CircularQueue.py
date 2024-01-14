import ctypes

class EmptyCircularQueueError(Exception):
    pass

class FullCircularQueueError(Exception):
    pass

class CircularQueue:
    def __init__(self, cap):
        self.cap = cap
        self.queue = self.make_array(cap)
        self.front = self.rear = 0

    def make_array(self, size):
        return (ctypes.py_object * size)()

    def next(self, pos):
        return (pos + 1) % self.cap

    def is_empty(self):
        return self.front ==  self.rear

    def is_full(self):
        return self.front == self.next(self.rear)

    def enqueue(self, elt):
        if self.is_full():
            raise FullCircularQueueError("Circular Queue is full!")
        else:
            self.queue[self.rear] = elt
            self.rear = self.next(self.rear)

    def dequeue(self):
        if self.is_empty():
            raise EmptyCircularQueueError("Circular Queue is empty!") 
        else:
            del_item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = self.next(self.front)
            return del_item
        
    def __str__(self):
        size = abs(self.rear - self.front)
        return str(self.queue)

cq = CircularQueue(5)
cq.enqueue(5)
cq.enqueue(10)
cq.enqueue(15)
cq.enqueue(20)
print(cq)
print(cq.dequeue())
print(cq)
print (cq.dequeue())
print(cq)
print (cq.rear, cq.front)
cq.enqueue(25)
print(cq)
cq.enqueue(30)
print(cq)