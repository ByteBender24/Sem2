lst = [10,9,8,7,6,5,4,3,2,1,0]

def merge_sort(lst):
    length = len(lst)
    if length <2 :
        return lst[:]
    else:
        mid = length//2
        return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))

def merge(lst1 , lst2):
    i=j=0
    res = []
    while (i<len(lst1)) and (j<len(lst2)):
        if (lst1[i] < lst2[j]):
            res.append(lst1[i])
            i += 1
        elif lst2[j] < lst1[i]: 
            res.append(lst2[j])
            j += 1
    
    if i < len(lst1):
        res.extend(lst1[i:])
    elif j < len(lst2):
        res.extend(lst2[j:])
    
    return res

print (merge_sort(lst))
print (lst)
