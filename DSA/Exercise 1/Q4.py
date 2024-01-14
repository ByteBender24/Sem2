'''Python's random module includes a function shuffle(data) that accepts a list of elements and randomly
reorders the elements so that each possible order occurs with equal probability. The random module includes a more basic function randint(a, b) that returns a uniformly random integer from a to b (including
both endpoints). Using only the randint function, implement your own version of the shuffle function.'''

#CREATOR INFO:
#ROLL NO :3122225002042
#NAME    : Harishraj S
#SECTION : IT A

#DATE CREATED : 09-04-2023

'''About shuffle method in random module:
CODE:
import random

my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

random.shuffle(my_list)
print("Shuffled list:", my_list)

OUTPUT:
Original list: [1, 2, 3, 4, 5]
Shuffled list: [3, 5, 1, 4, 2]

the shuffle() method randomly rearranged the elements of the list. Note that each time you call the shuffle() method, you will get a different ordering of the list.'''


def shuffler(data_list):

    #shuffler(data_list) shuffles the list of data randomly using randint method from random module

    import random
    length_lst = len(data_list)
    for times in range(length_lst):
        elt1_idx = random.randint(0,length_lst-1)   #random index 1
        elt2_idx = random.randint(0,length_lst-1)   #random index 2
        data_list[elt1_idx] , data_list[elt2_idx] = data_list[elt2_idx] , data_list[elt1_idx]   #simultaneous assignment (swapped the elements in list)
    return data_list


if __name__ == "__main__":

    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.

    import random

    #no. of elements in random data list is taken as input from user.
    num = abs(int(input("Enter a number greater or equal to 10 for better shuffling to see \nEnter number of elements in the list: ")))
    #random data list is produced from given input
    data_list = []
    for times in range(num):
        data_list.append(random.randint(1,99))
    print (f"original data: {data_list}")

    #random data list is given as argument for function 'shuffler'
    print (f"shuffled data : {shuffler(data_list)}")
