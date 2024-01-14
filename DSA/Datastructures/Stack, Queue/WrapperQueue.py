class Empty(Exception):
    '''Exception raised when attempting to perform an operation on an empty queue.'''
    pass


class AdapterQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return f"Q:{str(self.queue)}"

    def peek(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        return self.queue[0]


# Driver Code
if __name__ == "__main__":
    q = AdapterQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    print(q)
    print(len(q))
    print(q.peek())
    q.dequeue()
    q.dequeue()
    print(q)
