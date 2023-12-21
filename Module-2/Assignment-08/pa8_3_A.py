def elementDistinctnessFast(L):
    l = L.copy()
    l.sort()
    n = len(l)
    low = 0
    high = len(l) - 1
    mid = (low+high) // 2

    if n in (0,1) : return True                                #First base case 
    elif n ==2 : return l[low] != l[high]                    #Second one
    elif n == 3 : return l[mid] not in (l[low],l[high])    #Third one
    elif l[mid] in (l[mid-1],l[mid+1]) : return False    #Fourth one
    left = elementDistinctnessFast(l[low:mid])
    right = elementDistinctnessFast(l[mid:high+1])

    return left and right

     

# print(elementDistinctnessFast([1,2,5,10,3,31,32,33,37,50,250]))
# print(elementDistinctnessFast([1,2]))
# print(elementDistinctnessFast([1]))
# print(elementDistinctnessFast([]))
# print(elementDistinctnessFast([1,2,5,2,10]))
# print(elementDistinctnessFast([10,1,2,10]))
# print(elementDistinctnessFast([1,2,5,10,3,31,32,33,37,5,250]))
# print(elementDistinctnessFast([2,2]))


# X = [1,2,5,2,10]
# X.sort()
# print(X)