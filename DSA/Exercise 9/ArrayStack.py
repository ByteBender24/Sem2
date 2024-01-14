'''
ARRAY IMPLEMENTATION OF Stack data structure
This is one of the ways to implement Stack data structure using array

Created by : Harishraj S
             IT A
             3122 22 5002 042

Contact    : <harishraj2210713@ssn.edu.in>
             
Date created : 10-06-2023

Modules imported:
    ctypes:
        ctypes module contains datatypes that mirrors those in C and C
        can also use functions, libraries related to C and C++
    array:
        for converting a list or tuple to array
'''

import ctypes
import array


class ArrayStack:

    '''
    Stack Implementation Using Arrays (ctypes)

    Methods present:
        __init__ --> constructor function
        __len__
        isEmpty
        push
        pop
        top
        get_capacity
        append
        resize
        count
        index
        __contains__
    '''

    def __init__(self, val=16):
        '''
            initializes the dynamic array with capacity and size, 
            uses ctypes.pyobject to create objects related to C datatypes

            Arguments:
                val:int - capacity of the dynamic array (default argument, equals to 16)
                val:tup or list - takes in the list or tuple of elements as its own elements
                val:str - takes the individual characters as its own elements

            Returns:
                None
        '''
        if isinstance(val, int):
            self.size = 0
            self.capacity = val
            self.items = (ctypes.py_object * val)()

        elif isinstance(val, tuple) or isinstance(val, list):
            self.size = len(val)
            self.capacity = len(val)
            self.items = array.array('i', val)

        elif isinstance(val, str):
            self.size = len(val)
            self.capacity = len(val)
            self.items = array.array('i', [i for i in val])

    def __len__(self):
        '''
            Returns the size of the list.

            Returns:
                The size of the list.
        '''
        return self.size

    def isEmpty(self):
        '''
            Checks whether the list is empty.

            Returns:
                True if the list is empty, False otherwise.
        '''
        return self.size == 0

    def top(self):
        '''
            Returns the ending position of the list.

            Returns:
                The ending position of the list.
        '''
        return self.items[self.size-1]

    def push(self, value=None):
        '''
            Appends a value to the end of the dynamic array.

            Arguments:
                val: The value to be appended.
        '''
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.items[self.size] = value
        self.size += 1

    def get_capacity(self):
        '''
            Returns the current capacity of the underlying array.

            Returns:
                The current capacity of the array.
        '''
        return self.capacity

    def resize(self, capacity):
        '''
            Resizes the underlying array to the specified capacity.

            Arguments:
                capacity (int): The new capacity of the array.

            Returns:
                None
        '''
        temp = (ctypes.py_object * capacity)()
        for index in range(self.size):
            temp[index] = self.items[index]
        self.items = temp
        self.capacity = capacity

    def __str__(self):
        '''
            Returns a string representation of the dynamic array.

            Returns:
                A string representation of the dynamic array.
        '''
        array_string = '<'
        for i in range(self.size):
            array_string += str(self.items[i])
            if i != self.size - 1:
                array_string += ','
        array_string += '>'
        return array_string

    def pop(self):
        '''
            Deletes an element at a given index in the array.

            Arguments:
                idx (int): The index of the element to delete.

            Raises:
                IndexError: If the index is out of range.
        '''
        self.items[self.size - 1] = None
        self.size -= 1
        if self.size < self.capacity // 4:  # if the size of the array is smaller than 25%, then shrink the array
            self.resize(self.capacity // 2)

    def __contains__(self, search_elt):
        '''
            Checks if an element is present in the dynamic array

            Arguments:
                search_elt: The element to be searched in the array

            Returns:
                bool: True, if the search element is present in the array, otherwise False.
        '''
        for idx in range(0, self.size):
            if self.items[idx] == search_elt:
                return True
        return False

        # return search_elt in self.items

    def index(self, elt):
        '''
            Checks if an element is present in the array and returns the index of the element

            Arguments:
                elt: Element whose index is to be found out

            Returns:
                idx (int): If the element is found, index of the element is returned, else -1.
        '''
        for idx in range(0, self.size):
            if self.items[idx] == elt:
                return idx
        return -1

    def count(self, count_elt):
        '''
            Returns the number of occurrences of an element in the dynamic array

            Arguments:
                count_elt: Element whose number of occurrences is to be found

            Returns:
                count (idx): The number of occurrences of an element in the dynamic array
        '''
        count = 0
        for idx in range(0, self.size):
            if self.items[idx] == count_elt:
                count += 1
        return count

#Driver Code:
if __name__ == "__main__":
    s = ArrayStack()
    s.push(1)
    s.push(2)
    s.push()
    s.push(4)
    print (len(s))
    print (s.isEmpty())
    print (s)
    s.pop()
    s.pop()
    print (s)