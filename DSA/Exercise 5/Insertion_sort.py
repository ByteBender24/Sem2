'''
This program performs insertion sort algorithm for a given list of elements

Insertion sort, takes the elements and compares with the previous sorted array, and places
it in the suitable index.

Time complexity = O(n²)

Created by : Harishraj S
             IT A
             3122 22 5002 042

Contact    : <harishraj2210713@ssn.edu.in>
             
Date created : 19-05-2023
'''

overwritecount = 0
comparisoncount = 0

def insertion_sort(lst):
    '''
        insertion_sort(lst), takes the elements and compares with the previous sorted array, and places
        it in the suitable index in the sorted part of array.

        Arguments:
                lst - unsorted list
                
        Returns:
            Original List (lst) is sorted
            Returns None
    '''

    global comparisoncount
    global overwritecount
    
    length = len(lst)

    for i in range(1,length):
        elt = lst[i]
        j = i-1
        while (j >= 0 and elt < lst[j]):
            comparisoncount += 1
            lst[j+1] = lst[j]
            overwritecount += 1
            j -= 1
        lst[j+1] = elt
    
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
        insertion_sort(lst)
        end = default_timer()

        timee = abs(start - end)
        print (lst , "\ntime=", timee)

        print (f"overwrite = {overwritecount} , comparison = {comparisoncount}")
        print ()

        overwritecount, comparisoncount = 0 , 0

        #worst cases
        lst.sort(reverse=True)
        print (f"{times + 1}) {lst}")

        start = default_timer()
        insertion_sort(lst)
        end = default_timer()

        timee = abs(start - end)
        print (lst , "\ntime=", timee)

        print (f"overwrite = {overwritecount} , comparison = {comparisoncount}")
        print ()

        overwritecount, comparisoncount = 0 , 0

        #best cases
        lst.sort()
        print (f"{times + 1}) {lst}")

        start = default_timer()
        insertion_sort(lst)
        end = default_timer()

        timee = abs(start - end)
        print (lst , "\ntime=", timee)

        print (f"overwrite = {overwritecount} , comparison = {comparisoncount}")
        print ()

        overwritecount, comparisoncount = 0 , 0    