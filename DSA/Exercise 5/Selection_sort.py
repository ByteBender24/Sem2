'''
This program performs selection sort algorithm for a given list of elements

Selection sort, finds the smallest number in the array and moves it to first index
then continues with the rest of the unsorted array till it is sorted.

Time complexity = O(n²)

Created by : Harishraj S
             IT A
             3122 22 5002 042

Contact    : <harishraj2210713@ssn.edu.in>
             
Date created : 19-05-2023
'''

comparisoncount = 0
swappingcount = 0

def selection_sort(lst):
    '''
        selection_sort(lst) takes list as input, finds the smallest number in the array and moves it to first index
        then continues with the rest of the unsorted array till it is sorted.
        
        Arguments:
            lst - unsorted list
            
        Returns:
            Original List (lst) is sorted
            Returns None
    '''

    global comparisoncount
    global swappingcount

    length = len(lst)

    for i in range(length):
        min_idx = i

        for j in range(i, length):
            comparisoncount += 1
            if lst[j] < lst[min_idx]:
                min_idx = j

        swappingcount += 1
        lst[min_idx] , lst[i] = lst[i] , lst[min_idx]

    return 

if __name__ == "__main__":
    import random
    from timeit import default_timer

    f = open("selectionsort_data.txt", 'w')
    
    elt = 10        #number of elements in the lst
    for times in range(10):

        # average cases
        lst = [random.randint(1,100) for i in range(elt)]       #using list comprehension, making a random list of elt no.of elements
        print (f"{times + 1}) {lst}", file = f)

        start = default_timer()
        selection_sort(lst)
        end = default_timer()

        timee = abs(start - end)
        print (lst , "\ntime=", timee, file = f)

        print (f"swapping = {swappingcount} , comparison = {comparisoncount}", file = f)
        print (file = f)

        swappingcount, comparisoncount = 0 , 0

        #worst cases
        lst.sort(reverse=True)
        print (f"{times + 1}) {lst}", file = f)

        start = default_timer()
        selection_sort(lst)
        end = default_timer()

        timee = abs(start - end)
        print (lst , "\ntime=", timee, file = f)

        print (f"swapping = {swappingcount} , comparison = {comparisoncount}", file = f)
        print (file = f)

        swappingcount, comparisoncount = 0 , 0

        #best cases
        lst.sort()
        print (f"{times + 1}) {lst}", file = f)

        start = default_timer()
        selection_sort(lst)
        end = default_timer()

        timee = abs(start - end)
        print (lst , "\ntime=", timee, file = f)

        print (f"swapping = {swappingcount} , comparison = {comparisoncount}", file = f)
        print (file = f)

        swappingcount, comparisoncount = 0 , 0

