def partition2(A,p,r):
    x = A[r]
    i1 = p-1
    i2 = p-1
    for j in range(p,r):
        if A[j]==x:
            i2 +=1
            (A[i2] , A[j]) = (A[j] , A[i2])
            if i1 == -1 : 
                i1 = i2
            
        elif A[j]<x:
            i2 +=1
            if i1 == -1 :
                (A[i2] , A[j]) = (A[j] , A[i2])
            else:
                (A[i1],A[i2]) = (A[i2] , A[i1])
                if j> i2 :
                    (A[i1],A[j])  = (A[j],A[i1])
                i1 +=1

    i2 +=1
    (A[r],A[i2])=(A[i2],A[r])
    return (i1,i2) if i1 != -1 else (i2 , i2)

# L = [75, 25, 56 , 81 , 75]
# L = [0,1,2,0,1,2,0,1,2,1]
L = [1,2,9,0,7,3,8,7,1,8,4,7,7]
# L = [0,1]
print(partition2(L , 0 , len(L)-1))
print(L)
partition2(L , 0 , )