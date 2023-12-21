def equalElements(M):
    m = len(M)
    n = len(M[0])
    D = {}

    for i in range(m):
        for j in range(n):
            if M[i][j] not in D : D[M[i][j]] = (i , j)
            else :   
                return ( D[M[i][j]] , (i,j) )   
    
    return ((-1,-1),(-1,-1))


# import numpy as np
# M1 = [[1,2],[3,4]]
# M2 = [[1,2],[3,1]]
# M3 = [[1,3,0,5],[2,5,2,-1],[5,6,-2,6]]
# M4 = [[1,3,0,5],[20,50,2,-1],[51,61,-2,16]]
# for M in (M1,M2,M3,M4):
#     print(np.matrix(M))
#     print(equalElements(M),"\n")

# import time
# start_time = time.time()
# m = [[39, 44, 54, -35, -36, -53, -14, -38, -27, 40], [21, 59, 33, -43, -61, 25, -17, 53, -40, -19], [64, 19, -47, 35, -36, -46, -25, -3, 0, -32], [62, 10, 12, 8, -23, -70, -4, -13, 29, -64], [-2, 57, 45, -33, -10, -20, 42, 3, 26, 22], [-39, -58, -52, 46, 43, 63, -68, -49, -60, -48], [23, 68, 56, -41, 69, 52, 41, 13, 61, 30]]
# print(equalElements(m))
# end_time = time.time()
# print(end_time-start_time)