def indexOfMin(L , start , end):
    mini = start
    for i in range(start+1 , end+1):
        if L[i] < L[mini]:
            mini = i
    return mini

L = [10,4,3,7,3,15]
print(indexOfMin(L,0,5))
print(indexOfMin(L,1,5))
print(indexOfMin(L,3,4))
print(indexOfMin(L,4,4))