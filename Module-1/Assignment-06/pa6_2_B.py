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


print("b) ")
L = [-6, 1, 3, 5, 7, 8, 9, 11]
print(linearSorted2Sum(L, 14)) # 7+7
print(linearSorted2Sum(L, 12)) # 1+11
print(linearSorted2Sum(L, 15)) # 7+8
print(linearSorted2Sum(L, 3)) # -6+3
print(linearSorted2Sum(L, 0))
print(linearSorted2Sum(L, 7))
print(linearSorted2Sum(L, 21))