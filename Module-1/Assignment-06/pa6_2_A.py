def sorted2Sum(L, t):
    for num in L:
        complement = t - num
        left, right = 0, len(L) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if L[mid] == complement:
                return True
            elif L[mid] < complement:
                left = mid + 1
            else:
                right = mid - 1

        if num * 2 == t:
            return True

    return False



print("a) ")
L = [-6, 1, 3, 5, 7, 8, 9, 11]
print(sorted2Sum(L, 14)) # 7+7
print(sorted2Sum(L, 12)) # 1+11
print(sorted2Sum(L, 15)) # 7+8
print(sorted2Sum(L, 3)) # -6+3
print(sorted2Sum(L, 0))
print(sorted2Sum(L, 7))
print(sorted2Sum(L, 21))
