def fIterative(n):
    global N
    N += 1
    L = [1 ,1 ,1 ] + [0]*(n-2)
    for i in range(3 ,n+1):
        L[i] = L[i-1] + L[i-2] + L[i-3] + L[i//3]

    return L[n]


N=0
print("\nf(25): ",fIterative(25))
print("Number of recursive calls for 25:", N)  