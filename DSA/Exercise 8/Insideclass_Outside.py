'''
This program is to implement methods inside the class and
implement general functions outside the class

Created by : Harishraj S
             IT A
             3122 22 5002 042

Contact    : <harishraj2210713@ssn.edu.in>
             
Date created : 10-06-2023
'''

# Implementation as methods inside a class


class MyList:
    def __init__(self, data):
        self.data = data

    def extend(self, other_list):
        self.data.extend(other_list)

    def contains(self, item):
        return item in self.data

    def index(self, item):
        if item not in self.data:
            raise ValueError("Item not found in the list")
        return self.data.index(item)

    def count(self, item):
        return self.data.count(item)

# Implementation as general functions outside the class


def extend_list(list1, list2):
    list1.extend(list2)


def contains_item(list1, item):
    return item in list1


def find_index(list1, item):
    if item not in list1:
        raise ValueError("Item not found in the list")
    return list1.index(item)


def count_item(list1, item):
    return list1.count(item)

# Driver code


def main():
    # List operations using methods
    my_list = MyList([1, 2, 3])
    my_list.extend([4, 5, 6])
    print(my_list.data)  # Output: [1, 2, 3, 4, 5, 6]
    print(my_list.contains(3))  # Output: True
    print(my_list.index(4))  # Output: 3
    print(my_list.count(2))  # Output: 1

    # List operations using general functions
    list1 = [1, 2, 3]
    extend_list(list1, [4, 5, 6])
    print(list1)  # Output: [1, 2, 3, 4, 5, 6]
    print(contains_item(list1, 3))  # Output: True
    print(find_index(list1, 4))  # Output: 3
    print(count_item(list1, 2))  # Output: 1


if __name__ == "__main__":
    main()
