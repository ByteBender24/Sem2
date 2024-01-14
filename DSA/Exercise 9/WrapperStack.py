class Empty(Exception):
    '''Exception raised when attempting to perform an operation on an empty stack.'''

    pass


class AdapterStack:
    '''
        AdapterStack is a wrapper class that provides a stack interface using a Python list as the underlying data structure.

        Attributes:
            items (list): A list to store the stack elements.

        Methods:
            __init__(): Initializes an empty stack.
            is_empty(): Checks if the stack is empty.
            push(item): Adds an item to the top of the stack.
            pop(): Removes and returns the topmost item from the stack.
            peek(): Returns the topmost item from the stack without removing it.
            size(): Returns the current size of the stack.
    '''

    def __init__(self):
        '''
            Initializes an empty stack.
        '''
        self.items = []

    def is_empty(self):
        '''
            Checks if the stack is empty.

            Returns:
                bool: True if the stack is empty, False otherwise.
        '''
        return len(self.items) == 0

    def __len__(self):
        '''
            Returns the length of the stack.

            Returns:
                int: The length of the stack.
        '''
        return len(self.items)

    def __str__(self):
        '''
            Returns a string representation of the stack.

            Returns:
                str: A string representation of the stack.
        '''
        return str(self.items)

    def push(self, item):
        '''
            Adds an item to the top of the stack.

            Arguments:
                item: The item to be added to the stack.
        '''
        self.items.append(item)

    def top(self):
        '''
            Returns the topmost element of the stack.

            Returns:
                The topmost element of the stack.

            Raises:
                Empty: If the stack is empty.
        '''
        if len(self.items) == 0:
            raise Empty("Stack is empty!")
        return self.items[-1]

    def pop(self):
        '''
            Removes and returns the topmost element from the stack.

            Returns:
                The topmost element of the stack.

            Raises:
                Empty: If the stack is empty.
        '''
        if len(self.items) == 0:
            raise Empty("Stack is empty!")
        return self.items.pop()

    def size(self):
        '''
            Returns the current size of the stack.

            Returns:
                int: The size of the stack.
        '''
        return len(self.items)

    def clear(self):
        '''
            Returns the empty stack

            Returns:
                empty stack
        '''
        self.items = []
        return self.items


# Driver Code:
if __name__ == "__main__":
    # Create an instance of the AdapterStack class and assign it to the variable stk
    stk = AdapterStack()

    stk.push(10)  # Push the value 10 onto the stack
    stk.push(20)  # Push the value 20 onto the stack
    stk.push(30)  # Push the value 30 onto the stack
    stk.push(40)  # Push the value 40 onto the stack
    stk.push(50)  # Push the value 50 onto the stack
    stk.push(60)  # Push the value 60 onto the stack

    print(stk)  # Print the string representation of the stack

    stk.pop()  # Pop (remove and return) the topmost element from the stack
    stk.pop()  # Pop (remove and return) the topmost element from the stack

    print(stk.top())  # Print the topmost element of the stack without removing it

    print(stk)  # Print the string representation of the stack

    print(stk.size())  # Print the current size (number of elements) of the stack

    # Print whether the stack is empty (True if empty, False otherwise)
    print(stk.is_empty())

    stk.clear()  # clearing the stack
    print(stk)  # prints the empty stack
    stk.top()  # raises the Empty Error
    stk.pop()  # raises the Empty Error
