def threeDistinct(L):
    if len(L) < 3:
        return False
    
    def recThreeDistinct(L,low,high):
        if low > high:
            return 0
        if L[low] == L[high]:
            return 1
        if high - low == 1 :
            return 2
        
        mid = (low+high)//2
        if L[low] == L[mid]:
            return 1 + recThreeDistinct(L, mid+1, high)
        elif L[mid] == L[high]:
            return 1 + recThreeDistinct(L, low, mid-1)
        else:
            return recThreeDistinct(L, low, mid) + recThreeDistinct(L, mid + 1, high)
    return recThreeDistinct(L, 0, len(L)-1) >= 3    







print(threeDistinct([]))
print(threeDistinct([1]))
print(threeDistinct([1,1]))
print(threeDistinct([1,10]))
print(threeDistinct([1,1,10]))
print(threeDistinct([1,1,10,10,10]))
print(threeDistinct([1,1,3,10,10,10]))
print(threeDistinct([1,1,3,10,10,10,10,10,10]))
print(threeDistinct([1,1,1,1,1,3,3,4,10]))