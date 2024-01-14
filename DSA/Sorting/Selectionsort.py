lst = [10,9,8,7,6,5,4,3,2,1,0]

comparisoncount = 0
swappingcount = 0

def selection_sort(lst):

    global comparisoncount
    global swappingcount

    for i in range(len(lst)):
        min_idx = i

        for j in range(i,len(lst)):
            comparisoncount += 1
            if lst[j] < lst[min_idx]:
                min_idx = j
        swappingcount += 1
        lst[min_idx], lst[i] = lst[i] , lst[min_idx]
    
    return lst

selection_sort(lst)
print (lst)
print (swappingcount, comparisoncount)