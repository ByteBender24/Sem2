class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = self.tail = Node()
        self.size = 0

    def isempty(self):
        return self.head == self.tail
    
    def append(self, item):
        temp = Node(item)
        self.tail.next = temp
        self.tail = self.tail.next
        self.size += 1
    
    def __str__(self):
        string = '<'
        pos = self.head.next
        while pos is not None:
            string += str(pos.item) + ","
            pos = pos.next
        return string + ">"

    def 