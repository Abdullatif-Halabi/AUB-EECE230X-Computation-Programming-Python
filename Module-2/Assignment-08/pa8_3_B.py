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