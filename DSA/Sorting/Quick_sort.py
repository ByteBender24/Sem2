'''
This program performs Quick sort algorithm for a given list of elements

Quick sort is a recursive sorting algorithm that divides an array into two halves, sorts them independently, and then merges the sorted halves to obtain a fully sorted array. It repeatedly divides the array until individual elements are reached, and then merges them in a sorted manner. This process continues until the entire array is sorted.

Time complexity = O(n log(n)) -- Best case and average case
                = O(n²) -- Worst case

Created by : Harishraj S
             IT A
             3122 22 5002 042

Contact    : <harishraj2210713@ssn.edu.in>
             
Date created : 24-05-2023
'''

count = 0

def quick_sort(seq, begin, end):
    if begin < end:

        k = partition(seq, begin, end - 1)

        quick_sort(seq, begin, k - 1)
        quick_sort(seq, k + 1, end)


def partition(seq, begin, end):

    global count

    find_median(begin, end, seq)

    pivot = seq[end]

    i = begin - 1
    for j in range(begin, end):
        count += 1
        if seq[j] <= pivot:
            i += 1
            seq[i], seq[j] = seq[j], seq[i]

    seq[i+1], seq[end] = seq[end], seq[i+1]

    return i+1


def find_median(begin, end, seq):
    '''
    This function finds the median element and movies it to the end of the list, so that
    it can be the pivot while using in the partition function.

    This changes the original sequence

    
    Arguments:
        begin: starting index from which median is to be found
        end: ending index up to which median is to be found
        seq: sequence of which median is to be found

    Returns:
        None
    '''

    mid = (begin + end) // 2
    if seq[begin] > seq[mid]:
        seq[begin], seq[mid] = seq[mid], seq[begin]
    if seq[mid] > seq[end]:
        seq[mid], seq[end] = seq[end], seq[mid]
    if seq[begin] > seq[end]:
        seq[begin], seq[end] = seq[end], seq[begin]

    seq[mid], seq[end] = seq[end], seq[mid]


if __name__ == "__main__":
    import random
    from timeit import default_timer

    f = open("quicksort_data.txt", 'w')
    
    elt = 10        #number of elements in the lst
    for times in range(10):

        # average cases
        lst = [random.randint(1,100) for i in range(elt)]       #using list comprehension, making a random list of elt no.of elements
        print (f"{times + 1}) {lst}")

        start = default_timer()
        quick_sort(lst, 0 ,len(lst))
        end = default_timer()

        timee = abs(start - end)
        print (lst , "\ntime=", timee)

        print (f"count= {count}")
        print (file = f)

        count = 0

        #worst cases
        lst.sort(reverse=True)
        print (f"{times + 1}) {lst}")

        start = default_timer()
        quick_sort(lst, 0 ,len(lst))
        end = default_timer()

        timee = abs(start - end)
        print (lst , "\ntime=", timee)

        print (f"count= {count}")
        print (file = f)

        count = 0

        #best cases
        lst.sort()
        print (f"{times + 1}) {lst}")

        start = default_timer()
        quick_sort(lst, 0 ,len(lst))
        end = default_timer()

        timee = abs(start - end)
        print (lst , "\ntime=", timee)

        print (f"count= {count}")
        print (file = f)

        count = 0



def partition(array, start, end):
    pivot = array[start]
    low = start+1
    high = end

    while True:
        while low<high and array[low] < pivot:
            low += 1

        while low<high and array[high] > pivot:
            high -= 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        
        else:
            break
    
    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return
    
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

array = [40, 20, 10, 80, 60, 50, 7, 30, 100]
quick_sort(array, 0, len(array)-1)

