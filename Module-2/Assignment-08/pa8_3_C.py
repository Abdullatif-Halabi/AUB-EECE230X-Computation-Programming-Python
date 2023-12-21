def twoSumFast(L, t) :
    L = L.copy()
    L.sort()
    n = len(L)
    low =0
    high = n-1
    mid = (low+high)//2
    
    if low > high : return False
    if n ==1 and 2*L[low] != t : return False
    if t in ( L[low] + L[high] , 2*L[low] , 2*L[high] )  : return True
    elif L[low] + L[high] < t : 
        return twoSumFast(L[low+1:],t)
    else :
        if t == L[low] + L[mid] : return True
        elif L[low] + L[mid] > t :
            return twoSumFast(L[low:mid],t)
        else : 
            return twoSumFast(L[:high],t)
        


def fourSumFast(L,t):
    L = L.copy()
    L.sort()
    n = len(L)
    low =0
    high = n-1
    mid = (low+high)//2


    if low > high : return False
    if n==1 : return 4*L[0] == t 
    if L[mid] + 3*L[high] < t : 
        if mid == n-2 : return fourSumFast([L[-1]],t)
        else : return fourSumFast(L[mid+1:] , t)
    elif L[low] + 3*L[high] < t : return fourSumFast(L[low+1:] , t)
    elif 3*L[low] + L[high] > t : return fourSumFast(L[:high] , t)
    else :
        
        for i in range(n) :    
            if ( 4*L[i] == t ) or  (t - 3*L[i]) in L   :
                return True
            elif twoSumFast(L[i+1:], t - 2*L[i] ) : 
                return  True
            else :
                for j in range(i+1 , n):
                    if twoSumFast(L , t-L[i]-L[j]): return True

        return False



# L = [13, 5, 7, 9, 112,16,27,31]
# L.sort()
# print(L)
# print(fourSumFast(L,24)) # 5+5+5+9
# print(fourSumFast(L,40)) # 13+13+5+9
# print(fourSumFast(L,62)) # 13+13+5+31
# print(fourSumFast(L,98)) # 13+27+27+31
# print(fourSumFast(L,0))
# print(fourSumFast(L,10))
# print(fourSumFast(L,29))
# print(fourSumFast(L,89))

# L = [-10, -6, -2]
# print(fourSumFast(L, t = -8))