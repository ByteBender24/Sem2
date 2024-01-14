lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

comparisoncount = 0
overwritecount = 0


def insertion_sort(lst):

    global comparisoncount
    global overwritecount

    length = len(lst)

    for i in range(1, length):
        temp = lst[i]
        j = i-1
        while (j >= 0) and (lst[j] > temp):
            comparisoncount += 1
            lst[j+1] = lst[j]
            overwritecount += 1
            j -= 1
        lst[j+1] = temp

    return


insertion_sort(lst)
print(lst)
print(comparisoncount, overwritecount)
