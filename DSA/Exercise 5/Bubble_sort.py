'''
This program performs bubble sort algorithm for a given list of elements

Bubble sort, compares the adjacent elements, swaps if the previous element is bigger than later
and bubbles the largest element to the last of the array. Then this continues for remaining unsorted array
till it is sorted.

Time complexity = O(n²)

Created by : Harishraj S
             IT A
             3122 22 5002 042

Contact    : <harishraj2210713@ssn.edu.in>
             
Date created : 19-05-2023
'''

swappingcount = 0
comparisoncount = 0

def bubble_sort(lst):
    '''
        bubble_sort(lst) takes list as input,compares the adjacent elements, swaps if the previous element is bigger than later
        and bubbles the largest element to the last of the array. Then this continues for remaining unsorted array
        till it is sorted.
        
        Arguments:
            lst - unsorted list
            
        Returns:
            Original List (lst) is sorted
            Returns None
    '''

    global swappingcount
    global comparisoncount

    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            comparisoncount += 1
            if lst[j] > lst[j+1]:
                swappingcount += 1
                lst[j] , lst[j+1] = lst[j+1] , lst[j]

    return 

if __name__ == "__main__":
    import random
    from timeit import default_timer

    elt = 10        #number of elements in the lst
    for times in range(10):

        # average cases
        lst = [random.randint(1,100) for i in range(elt)]       #using list comprehension, making a random list of elt no.of elements
        print (f"{times + 1}) {lst}")

        start = default_timer()
        bubble_sort(lst)
        end = default_timer()

        timee = abs(start - end)
        print (lst , "\ntime=", timee)

        print (f"swapping = {swappingcount} , comparison = {comparisoncount}")
        print ()

        swappingcount, comparisoncount = 0 , 0

        #worst cases
        lst.sort(reverse=True)
        print (f"{times + 1}) {lst}")

        start = default_timer()
        bubble_sort(lst)
        end = default_timer()

        timee = abs(start - end)
        print (lst , "\ntime=", timee)

        print (f"swapping = {swappingcount} , comparison = {comparisoncount}")
        print ()

        swappingcount, comparisoncount = 0 , 0

        #best cases
        lst.sort()
        print (f"{times + 1}) {lst}")

        start = default_timer()
        bubble_sort(lst)
        end = default_timer()

        timee = abs(start - end)
        print (lst , "\ntime=", timee)

        print (f"swapping = {swappingcount} , comparison = {comparisoncount}")
        print ()

        swappingcount, comparisoncount = 0 , 0
