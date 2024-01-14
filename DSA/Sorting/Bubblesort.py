 # lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# swappingcount = 0
# comparisoncount = 0


# def bubble_sort(lst):

#     global swappingcount
#     global comparisoncount

#     for i in range(len(lst)):
#         for j in range(len(lst) - i - 1):
#             comparisoncount += 1
#             if lst[j] > lst[j+1]:
#                 swappingcount += 1
#                 lst[j], lst[j+1] = lst[j+1], lst[j]

#     return lst


# print(bubble_sort(lst))
# print(swappingcount, comparisoncount)



lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

swappingcount = 0
comparisoncount = 0

def bubble_sort(lst):
    global swappingcount
    global comparisoncount
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            comparisoncount += 1
            if lst[j] > lst[j+1]:
                swappingcount += 1
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print(bubble_sort(lst))
print(swappingcount, comparisoncount) 
 