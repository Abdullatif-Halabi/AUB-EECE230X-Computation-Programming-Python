L=[5, 2, 4, 6, 1, 3 , 8 , 1]
n = len(L)

for i in range(n):
    for j in range(i+1 , n):
        if L[j] < L[i]:
            (L[i] , L[j]) = (L[j] , L[i])
            
print(L)