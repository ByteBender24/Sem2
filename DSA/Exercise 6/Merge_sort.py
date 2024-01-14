'''
This program performs Merge sort algorithm for a given list of elements

Merge sort is a recursive sorting algorithm that divides an array into two halves, sorts them independently, and then merges the sorted halves to obtain a fully sorted array. It repeatedly divides the array until individual elements are reached, and then merges them in a sorted manner. This process continues until the entire array is sorted.

Time complexity = O(n log(n))

Created by : Harishraj S
             IT A
             3122 22 5002 042

Contact    : <harishraj2210713@ssn.edu.in>
             
Date created : 24-05-2023
'''

count = 0

def merge(seq1, seq2):
    '''
    This function performs merge operation on the two lists which are passsed to the function.

    Arguments:
        seq1 : First sequence to be merged
        seq2 : Second sequence to be merged

    Returns:
        Merged list of seq1 and seq2 which is sorted
    '''

    global count
    i = j = 0
    m = len(seq1)
    n = len(seq2)
    result = []
    while i < m and j < n:
        count += 1
        if seq1[i] < seq2[j]:
            result.append(seq1[i])
            i += 1
        else:
            result.append(seq2[j])
            j += 1
    while (i < m):
        result.append(seq1[i])
        i += 1
    while (j < n):
        result.append(seq2[j])
        j += 1
    return result


def merge_sort(seq):
    '''
    Performs recursive merge operation on list by using divide and conquer technique
    
    Arguments:
        seq - list to be sorted
    
    Returns:
        Sorted sequence
    '''
    length = len(seq)
    if length < 2:  # Base Condition
        return seq[:]
    else:
        mid = length // 2
        return merge(merge_sort(seq[:mid]), merge_sort(seq[mid:]))  # Recursive call
    
if __name__ == "__main__":
    import random
    from timeit import default_timer

    f = open("mergesort_data.txt" , 'w')

    elt = 10        #number of elements in the lst
    for times in range(10):

        # average cases
        lst_orig = [random.randint(1,100) for i in range(elt)]       #using list comprehension, making a random list of elt no.of elements
        print (f"{times + 1}) {lst_orig}" , file = f)

        start = default_timer()
        lst_new = merge_sort(lst_orig)
        end = default_timer()

        timee = abs(start - end)
        print (lst_new , "\ntime=", timee , file = f)

        print (f"count = {count}" , file = f)
        print (file = f)

        count = 0


        #worst cases
        lst_orig.sort(reverse=True)
        print (f"{times + 1}) {lst_orig}", file = f)

        start = default_timer()
        lst_new = merge_sort(lst_orig)
        end = default_timer()

        timee = abs(start - end)
        print (lst_new , "\ntime=", timee, file = f)

        print (f"count = {count}", file = f)
        print ( file = f)

        count = 0

        #best cases
        lst_orig.sort()
        print (f"{times + 1}) {lst_orig}", file = f)

        start = default_timer()
        lst_new = merge_sort(lst_orig)
        end = default_timer()

        timee = abs(start - end)
        print (lst_new , "\ntime=", timee, file = f)

        print (f"count = {count}", file = f)
        print (file = f)
        
        count = 0
