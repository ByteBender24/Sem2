class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = Node()
        self.end = Node()
        self.size = 0

    def isempty(self):
        # return (self.size == 0)           #instead of using .size use with head and end mostly as .size is used for our convenience
        return self.head == self.end

    def display(self):
        pos = self.head
        while pos.next is not None:
            pos = pos.next
            print(pos.item)

    def append(self, item):
        self.end.next = Node(item, self.end.next) #here the second self.end.next is None, or we can also use None (but for reusability)
        self.end = self.end.next
        self.size += 1


# Driver Code
if __name__ == "__main__":
    ll = Linkedlist()
    ll.append(20)
    ll.append(30)
    ll.append(40)

    ll.display()