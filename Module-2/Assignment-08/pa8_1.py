def searchHybrid(L,x): # Wrapper function
    low = 0
    high = len(L)-1

    def linearSearch(L,x,low,high):
        index = -1
        for i in range(low,high+1) :
            if L[i] == x:
                return i
        return index
        
    def recBinarySearchHybrid(L,x,low, high):
        if high-low+1 <= 5 :
            return linearSearch(L,x,low,high)
        else :
            if low > high : return -1
            mid = (low+high) // 2
            if L[mid] == x:  
                return mid
            elif L[mid] > x :
                return recBinarySearchHybrid(L,x,low,mid-1)
            else:
                return recBinarySearchHybrid(L,x,mid+1,high)
           
    return recBinarySearchHybrid(L,x,low,high)