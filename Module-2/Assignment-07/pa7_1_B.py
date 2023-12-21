def fMemoized(n):
    assert int(n) == n and n >= 0 , 'Bad input !'
    def recFMemoized(n,L):
        global N
        N += 1 
        if n in (0 ,1 , 2) : return 1
        else :
            if L[n] != 0 :
                return  L[n]
            else :
                L[n] = recFMemoized(n-1 , L) + recFMemoized(n-2 , L) + recFMemoized(n-3 , L) + recFMemoized(n//3 , L)
        return L[n]

    L = [0] * (n+1)  
    return recFMemoized(n ,L)  


N=0
print("\nf(25): ",fMemoized(25))
print("Number of recursive calls for 25:", N)  