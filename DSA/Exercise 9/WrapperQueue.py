class Empty(Exception):
    '''Exception raised when attempting to perform an operation on an empty queue.'''
    pass


class AdapterQueue:
    def __init__(self):
        '''Initialize an empty queue.'''
        self.queue = []

    def enqueue(self, value):
        '''
            Add an item to the end of the queue.

            Arguments:
                value: The item to be added to the queue.
        '''
        self.queue.append(value)

    def dequeue(self):
        '''
            Remove and return the item at the front of the queue.
            Returns:
                The item at the front of the queue.
            Raises:
                Empty: If the queue is empty.
        '''
        if self.is_empty():
            raise Empty("Queue is empty!")
        return self.queue.pop(0)

    def is_empty(self):
        '''
            Check if the queue is empty.
            Returns:
                True if the queue is empty, False otherwise.
        '''
        return len(self.queue) == 0

    def __len__(self):
        '''
            Return the number of items in the queue.
            Returns:
                The number of items in the queue.
        '''
        return len(self.queue)

    def __str__(self):
        '''
            Return a string representation of the queue.
            Returns:
                A string representation of the queue.
        '''
        return f"Q:{str(self.queue)}"

    def peek(self):
        '''
            Return the item at the front of the queue without removing it.
            Returns:
                The item at the front of the queue.
            Raises:
                Empty: If the queue is empty.
        '''
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
