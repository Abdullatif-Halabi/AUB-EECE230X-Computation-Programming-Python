def insertionSort(L):
    n = len(L)
    for j in range(1 , n):
        key = L[j]
        i = j-1
        while i >= 0 and L[i] > key :
            (L[j] , L[i]) = (L[i] , key)
            i -= 1
            j -= 1
    return L

def linearSorted2Sum(L, t):
    left = 0
    right = len(L) - 1
    while left <= right:
        current_sum = L[left] + L[right]

        if L[left]*2 == t or L[right]*2 == t or current_sum == t:
            return True
        elif current_sum < t:
            left += 1
        else:
            right -= 1
            
    return False

def fast3Sum(L,t) :
    insertionSort(L)
    for num in L:
        complement = t - num
        if linearSorted2Sum(L,complement)  :
                return True

    return False

print("c) ")
L = [-6, 1, 3, 5, 7, 9, 11]
print(fast3Sum(L,2)) # e.g., -6+1+7
print(fast3Sum(L,5)) # e.g., 1+1+3
print(fast3Sum(L,7)) # e.g., 1+1+5
print(fast3Sum(L,15)) # e.g., 1+3+11
print(fast3Sum(L,19)) # e.g., 3+7+9
print(fast3Sum(L,0))
print(fast3Sum(L,1))
print(fast3Sum(L,18))
print(fast3Sum(L,20))
print(fast3Sum(L,28))