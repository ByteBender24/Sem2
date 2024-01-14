from Merge_sort import merge_sort

count = 0

def binarysearch(seq, low, high, search_elt):
    global count
    """
    This function finds the search element in a sequence recursively using binary search
    """
    count += 1
    if low > high:  # base condition
        return -1
    else:
        mid = (low + high) // 2
        count += 1
        if search_elt == seq[mid]:
            return mid
        count += 1
        if search_elt < seq[mid]:
            return binarysearch(seq, low, mid - 1, search_elt)
        else:
            return binarysearch(seq, mid + 1, high, search_elt)


if __name__ == "__main__":
    import random

    size = int(input("Enter the size of the list: "))
    seq = [random.randint(-10000, 10000) for _ in range(size)]
    search_elt = random.choice(seq)
    print(search_elt)
    print(merge_sort(seq))
    print(binarysearch(merge_sort(seq), 0, size, search_elt))
    print(size, count)