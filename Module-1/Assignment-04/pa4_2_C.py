def indexOfMin(L , start , end):
    mini = start
    for i in range(start+1 , end+1):
        if L[i] < L[mini]:
            mini = i
    return mini

def selectionSort(L):
    n = len(L)
    for i in range(n-1):
        j = indexOfMin(L , i+1, n-1)
        if L[j] < L[i]:
            (L[i] , L[j]) = (L[j] , L[i])



L = [10,4,3,7,3,15]
selectionSort(L)
print(L)
L = [1.1, 31.31, 5.15]
selectionSort(L)
print(L)
L = [10, 10]
selectionSort(L)
print(L)
L = [1]
selectionSort(L)
print(L)
L = []
selectionSort(L)
print(L)