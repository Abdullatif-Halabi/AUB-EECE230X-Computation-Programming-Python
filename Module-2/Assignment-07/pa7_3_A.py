# def recursionWrapper(L):
def recursiveModeFinder(L, low, high):
    mid = (low + high) // 2
    if low == high : return low
    elif L[mid] > L[mid+1] :
        return recursiveModeFinder(L, low, mid)
    elif L[mid] < L[mid+1] :
        return recursiveModeFinder(L, mid+1, high)
    # return recursiveModeFinder(L, 0, len(L)-1)

# L1 = [1,2,5,20]
# L2 =[50,2,1]
# L3 = [1]
