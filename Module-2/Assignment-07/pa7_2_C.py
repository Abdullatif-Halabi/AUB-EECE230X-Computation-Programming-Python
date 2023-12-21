def multMatrices(A,B):
    """ A and B are lists of lists representing two 2 by 2 matrices"""
    C00 = A[0][0]*B[0][0]+A[0][1]*B[1][0]
    C01 = A[0][0]*B[0][1]+A[0][1]*B[1][1]
    C10 = A[1][0]*B[0][0]+A[1][1]*B[1][0]
    C11 = A[1][0]*B[0][1]+A[1][1]*B[1][1]
    C = [[C00, C01], [C10, C11]]
    return C

def fibMatrixVersion(n): 
    assert int(n)==n and n>=0 , "n should be a non-negative integer "
    def recMatrixPowerFast(X,n):
        """ X is a list of lists representing a 2 by 2 matrix and n is non-negative integer"""
        if n==0: return [[1,0],[0,1]]
        elif n == 1 : return [[1,1],[1,0]]
        elif n == 2 : return multMatrices(X,X)
        else:
            half_pow = recMatrixPowerFast(X, n // 2)

            if n%2 == 0 :
                return multMatrices(half_pow , half_pow)
            else :
                A = multMatrices(half_pow,half_pow)
                return multMatrices(X,A)
        
    X = [[1,1],[1,0]]    
    C = recMatrixPowerFast(X,n)
    return C[0][1]


# for i in range(11):
#     print("F_",i,":", fibMatrixVersion(i))
# print("F_ 100 :", fibMatrixVersion(100))

# a = [[30, -27], [-10, 28]]
# b = [[23, 17], [0, -9]]
# print(multMatrices(a,b))