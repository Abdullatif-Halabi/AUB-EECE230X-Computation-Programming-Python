# def linearSorted2Sum(L,t):  #O(n)
#     """ assumes L is sorted"""
#     n = len(L)
#     i = 0
#     j = n-1
#     while i <= j: 
#         if L[i]+L[j]==t: 
#             return True
#         elif L[i]+L[j]>t:  
#             j-=1
#         else: 
#             i+=1
#     return False 


# def twoSumFast(L, t) :
#     l = L.copy()
#     l.sort()
#     n = len(l)
#     low =0
#     high = n-1
#     mid = (low+high)//2

#     if n in (1,0):
#         return linearSorted2Sum(l,t)                #First base case
#     elif n == 2 : return linearSorted2Sum(l,t)      #Second base case
#     elif 2*l[mid] == t : return True                #Third base case
#     elif 2*l[mid] > t : return twoSumFast(l[low:mid+1] , t)     
#     else:
#         return twoSumFast(l[mid :high+1] , t)
    


# L = [8,1, 3, 11, 5, 7,-6 , 9]
# L.sort()
# print(L)
# print(twoSumFast(L, 14)) # 7+7
# print(twoSumFast(L, 12)) # 1+11
# print(twoSumFast(L, 15)) # 7+8
# print(twoSumFast(L, 3)) # -6+3
# print(twoSumFast(L, 0))
# print(twoSumFast(L, 7))
# print(twoSumFast(L, 21))

# L = [18, 12, 16, 14, 2, 10, 7, 10, 20, 17, 10, 14, 18, 14, 9, 17, 1, 20, 9]
# L.sort()
# print(L)
# print(twoSumFast(L,23))

#####################################################
def linearSorted2Sum(L,t):  #O(n)
    """ assumes L is sorted"""
    n = len(L)
    i = 0
    j = n-1
    while i <= j: 
        if L[i]+L[j]==t: 
            return True
        elif L[i]+L[j]>t:  
            j-=1
        else: 
            i+=1
    return False 


def twoSumFast(L, t) :
    l = L.copy()
    l.sort()
    n = len(l)
    low =0
    high = n-1
    mid = (low+high)//2
    if n ==1 and 2*L[low] != t : return False
    if t in ( l[low] + l[high] , 2*l[low] , 2*l[high] )  : return True
    elif l[low] + l[high] < t : 
        return twoSumFast(l[low+1:],t)
    else :
        if t == l[low] + l[mid] : return True
        elif l[low] + l[mid] > t :
            return twoSumFast(l[low:mid],t)
        else : 
            return twoSumFast(l[:high],t)
                

# L = [18, 12, 16, 14, 2, 10, 7, 10, 20, 17, 10, 14, 18, 14, 9, 17, 1, 20, 9]
# print(twoSumFast(L,23))
# L.sort()
# print(L)


L = [8,1, 3, 11, 5, 7,-6 , 9]
L.sort()
print(L)
print(twoSumFast(L, 14)) # 7+7
print(twoSumFast(L, 12)) # 1+11
print(twoSumFast(L, 15)) # 7+8
print(twoSumFast(L, 3)) # -6+3
print(twoSumFast(L, 0))
print(twoSumFast(L, 7))
print(twoSumFast(L, 21))

# print(twoSumFast([20] , 40))