import ctypes

class EmptyError(Exception):
    pass

class FullError(Exception):
    pass

class TwoWayStack:

    def __init__(self, cap=16):
        self.capacity = cap
        self.size = 0
        self.top1 = 0
        self.top2 = self.capacity - 1
        self.items = (ctypes.py_object * cap)()

    def isempty(self):
        return self.size == 0
    
    def isfull(self):
        return self.size == self.capacity
    
    def push(self, stack_no = 0, item=None):
        if self.isfull():
            raise FullError("Stack is full")
        if stack_no == 0:
            self.items[self.top1] = item
            self.top1 += 1
            self.size += 1
        elif stack_no == 1:
            self.items[self.top2] = item
            self.top2 -= 1
            self.size += 1

    def pop(self, stack_no = 0):
        if self.isempty:
            raise EmptyError("Stack is empty")
        if stack_no == 0:
            self.items[self.top1 - 1] = None
            self.top1 -= 1
            self.size -= 1
        elif stack_no == 1:
            self.items[self.top2 + 1] = None
            self.top2 += 1
            self.size -= 1

    def __str__(self):
        string = "<Stack 1: "
        for i in range(self.top1):
            string += str(self.items[i]) + ", "
        string = string.rstrip(", ")  # Remove trailing comma and space
        string += "> | <Stack 2: "
        for i in range(self.capacity - 1, self.top2, -1):
            string += str(self.items[i]) + ", "
        string = string.rstrip(", ")  # Remove trailing comma and space
        string += ">"
        return string

q = TwoWayStack()
q.push(0,1)
print (q)

q.push(0,2)
print (q)

q.push(0,3)       
print (q)

q.push(0,4)       
print (q)

q.push(0,5)       
print (q)

q.push(1,1)       
print (q)

q.push(1,2)       
print (q)

q.push(1,3)       
print (q)

q.push(1,4)       
print (q)

q.push(1,5)       
print (q)

q.push(0,6)       
print (q)

q.push(0,7)       
print (q)

q.push(0,8)       
print (q)

q.push(0,9)       
print (q)

q.push(0,10)
q.push(0,11)
print (q)

q.push(1,12)
    