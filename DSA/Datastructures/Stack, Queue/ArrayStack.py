import ctypes
import array


class ArrayStack:

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
            self.items = array.array('i', [i for i in val])

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def top(self):
        return self.items[self.size-1]

    def push(self, value=None):
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

    def pop(self):
        self.items[self.size - 1] = None
        self.size -= 1
        if self.size < self.capacity // 4:
            self.resize(self.capacity // 2)

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


# Driver Code:
if __name__ == "__main__":
    s = ArrayStack()
    s.push(1)
    s.push(2)
    s.push()
    s.push(4)
    print(len(s))
    print(s.isEmpty())
    print(s)
    s.pop()
    s.pop()
    print(s)
