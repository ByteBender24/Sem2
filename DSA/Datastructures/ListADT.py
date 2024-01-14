import ctypes
import array


class ArrayList:

    '''
    Dynamic array list object can be implemented by this class Arraylist

    Methods present:
        __init__ --> constructor function
        __len__
        __setitem__
        __getitem__
        isEmpty
        next
        begin
        end
        get_capacity
        append
        resize
        count
        index
        __contains__
    '''

    def __init__(self, val=16):
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
            self.items = array.array('u', [i for i in val])

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if 0 <= index < self.size == False:
            raise IndexError("Index is out of range!")
        return self.items[index]

    def __setitem__(self, value, index):
        if (0 <= index < self.size) == False:
            raise IndexError("Index is out of range!")
        else:
            self.items[index] = value

    def isEmpty(self):
        return self.size == 0

    def next(self, pos):
        if (0 <= pos < self.size) == False:
            raise IndexError("Index is out of range!")
        return self.items[pos + 1]

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.iter_index >= self.size:
            raise StopIteration
        value = self.items[self.iter_index]
        self.iter_index += 1
        return value
    
    def begin(self):
        return 0

    def end(self):
        return self.size

    def append(self, value):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.items[self.size] = value
        self.size += 1

    def get_capacity(self):
        return self.capacity

    def resize(self, capacity):
        temp = (ctypes.py_object * capacity)()
        for index in range(self.size):
            temp[index] = self.items[index]
        self.items = temp
        self.capacity = capacity

    def __str__(self):
        array_string = '<'
        for i in range(self.size):
            array_string += str(self.items[i])
            if i != self.size - 1:
                array_string += ','
        array_string += '>'
        return array_string

    def insert(self, idx, elt):
        if (not 0 <= idx <= self.size):
            raise IndexError("Index out of range!")
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        for i in range(self.size, idx, -1):
            self.items[i] = self.items[i - 1]
        self.items[idx] = elt
        self.size += 1

    def delete(self, idx):
        if not 0 <= idx < self.size:
            raise IndexError("Index out of range!")
        for i in range(idx, self.size - 1):
            self.items[i] = self.items[i + 1]
        self.size -= 1
        if self.size < self.capacity // 4:  # if the size of the array is smaller than 25%, then shrink the array
            self.resize(self.capacity // 2)

    def extend(self, lst):
        for element in lst:
            self.append(element)

    def __contains__(self, search_elt):
        for idx in range(0, self.size):
            if self.items[idx] == search_elt:
                return True
        return False

    def index(self, elt):
        for idx in range(0, self.size):
            if self.items[idx] == elt:
                return idx
        return -1

    def count(self, count_elt):
        count = 0
        for idx in range(0, self.size):
            if self.items[idx] == count_elt:
                count += 1
        return count


# driver code
if __name__ == "__main__":
    import random

    d1 = ArrayList(10)
    d2 = ArrayList([1, 2, 3, 4])
    d3 = ArrayList('Hello')
    # for i in range(5):
    #     d1.append(random.randint(0, 100))
    d1.append(10)
    d1.append(20)
    d1.append(30)
    d1.append(40)
    d1.append(50)
    print(len(d1))
    print(d1[2])
    print(d1)
    d1.insert(2, -5)
    print(d1)
    d1.insert(6, 25)
    print(d1)
    d1.delete(6)
    print(d1)
    d1.extend([1, 2, 3, 4, 5, 6, 4])
    print(d1)
    print(2 in d1)
    print(d1.index(5))
    print(d1.count(4))

    # 2
    d2.append(10)
    d2.append(20)
    d2.append(30)
    d2.append(40)
    d2.append(50)
    print(len(d2))
    print(d2[2])
    print(d2)
    d2.insert(2, -5)
    print(d2)
    d2.insert(6, 25)
    print(d2)
    d2.delete(6)
    print(d2)
    d2.extend([1, 2, 3, 4, 5, 6, 4])
    print(d2)
    print(2 in d2)
    print(d2.index(5))
    print(d2.count(4))

    d3.append(10)
    d3.append(20)
    d3.append(30)
    d3.append(40)
    d3.append(50)
    print (len(d3))
    print (d3[2])
    print(d3)
    d3.insert(2, -5)
    print(d3)
    d3.insert(6, 25)
    print(d3)
    d3.delete(6)
    print(d3)
    d3.extend(ArrayList([1, 2, 3, 4, 5, 6, 4]))
    print(d3)
    print(2 in d3)
    print(d3.index(5))
    print(d3.count(4))
