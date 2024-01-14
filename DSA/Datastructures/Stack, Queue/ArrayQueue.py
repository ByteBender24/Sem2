import ctypes

class EmptyArrayQueue(Exception):
    pass

class ArrayQueue:

    def __init__(self, cap=16):
        self.capacity = cap
        self.rear = 0
        self.size = 0
        self.items = (ctypes.py_object * cap)()

    def resize(self, size):
        temp = (ctypes.py_object * size)()
        for i in range(self.rear):
            temp[i] = self.items[i]
        self.capacity = size
        self.items = temp

    def is_empty(self):
        return (self.rear == 0)
    
    def enqueue(self, item):
        if self.rear == self.capacity:
            self.resize(self.capacity * 2)
        self.items[self.rear] = item
        self.rear += 1
    
    def dequeue(self):
        if self.rear == self.capacity:
            raise EmptyArrayQueue("Empty Queue!")
        temp = self.items[0]
        for i in range(self.rear - 1):
            self.items[i] = self.items[i+1]
        self.rear -= 1
        if self.rear < self.capacity//4:
            self.resize(self.capacity//2)
        return temp
    
    def __str__(self):
        array_string = '<'
        for i in range(self.rear):
            array_string += str(self.items[i])
            if i != self.rear - 1:
                array_string += ','
        array_string += '>'
        return array_string
    
    def __len__(self):
        return self.rear
    
#Driver code
if __name__ == "__main__":
    q = ArrayQueue()
    q.enqueue(1)
    q.enqueue(2)    
    q.enqueue(3)    
    q.enqueue(4)    
    q.enqueue(5)
    print (len(q))
    print (q)
    q.dequeue()
    print (q)
    q.dequeue()
    print (q)
    q.dequeue()
    print (q)
    q.dequeue()
    print (q)
    q.dequeue()
    print (q)