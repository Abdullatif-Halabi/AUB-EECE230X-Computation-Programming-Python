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

def binarySearchFirstAndLastOccurrences(L,x) :
    i1 = binarySearchFirstOccurrence(L,x)
    if not L :
        i2= -1
    n = len(L)
    low = 0
    high = n-1
    i2 = -1
    while low <= high:
        mid = (high + low) // 2
        if L[mid] < x :
            low = mid + 1
        elif L[mid] > x :
            high = mid - 1
        else : 
            i2 = mid
            low = mid +1
    return (i1 , i2)

print(binarySearchFirstAndLastOccurrences([], 3))
print(binarySearchFirstAndLastOccurrences([5], 3))
print(binarySearchFirstAndLastOccurrences([5], 5))
print(binarySearchFirstAndLastOccurrences([3,5,5,5], 5))
print(binarySearchFirstAndLastOccurrences([3,5,5,5,5], 1))
print(binarySearchFirstAndLastOccurrences([3,5,5,5,5], 2))
print(binarySearchFirstAndLastOccurrences([3,5,7,7,7,15,26,30,33], 7))
print(binarySearchFirstAndLastOccurrences([3,5,7,7,7,15,26,30,33], 33))
print(binarySearchFirstAndLastOccurrences([3,5,7,7,7,15,26,30,33], 12))
print(binarySearchFirstAndLastOccurrences([3,3,5,7,15,26,30,33], 26))
print(binarySearchFirstAndLastOccurrences([3,3,3,3,3,3,3,3,3,3], 3))