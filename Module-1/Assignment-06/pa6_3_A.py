def binarySearchFirstOccurrence(L,x):
    if not L :
            return -1
    n = len(L)
    low = 0
    high = n-1
    index = -1
    while low <= high:
        mid = (high + low) // 2
        if L[mid] < x :
            low = mid + 1
        elif L[mid] > x :
            high = mid - 1
        else : 
            index = mid
            high = mid -1
    return index

# print(binarySearchFirstOccurrence([], 3))
# print(binarySearchFirstOccurrence([5], 3))
# print(binarySearchFirstOccurrence([5], 5))
# print(binarySearchFirstOccurrence([3,5,5,5], 5))
# print(binarySearchFirstOccurrence([3,5,5,5,5], 1))
# print(binarySearchFirstOccurrence([3,5,5,5,5], 2))
# print(binarySearchFirstOccurrence([3,5,7,7,7,15,26,30,33], 7))
# print(binarySearchFirstOccurrence([3,5,7,7,7,15,26,30,33], 33))
# print(binarySearchFirstOccurrence([3,5,7,7,7,15,26,30,33], 12))
# print(binarySearchFirstOccurrence([3,3,5,7,15,26,30,33], 26))
# print(binarySearchFirstOccurrence([3,3,3,3,3,3,3,3,3,3], 3))