def longestZeroSumSubList(L):
    n = len(L)
    if n==0 : return []

    iMax = 0
    jMax = -1
    D = {0:0}
    cumulativeSum = 0
    for i in range(1,n+1):
        cumulativeSum += L[i-1]
        if cumulativeSum not in D:
            D[cumulativeSum] = i
        else :
            if i-D[cumulativeSum] > jMax-iMax:
                iMax = D[cumulativeSum]
                jMax = i
                # D[cumulativeSum] = i
    return [] if (iMax , jMax) == (0,-1) else L[iMax:jMax]



# print(longestZeroSumSublist(L=[1, 10, -1, -1, 2, 3, -5, 26]))
# print(longestZeroSumSublist([1 ,10, -1, -1, 4, 3, -5, 26]))
# print(longestZeroSumSublist([1, 10, 1, -1, 4, 3, -5, 26]))
# print(longestZeroSumSublist([1, 10, 1, 0, 4, 3, -5, 26]))
# print(longestZeroSumSublist([1, 10, 1, 1, 4, 3, -5, 26]))
# print(longestZeroSumSublist([-1, -1, 2, 3, -5, 26]))
# print(longestZeroSumSublist([2, 2, -1, 0, -1, 2]))
# print(longestZeroSumSublist([1, 0, -2, 1, 0, 1, -1, 0, -1, 2, -2, -2]))

# print(longestZeroSumSublist(L=[1, 2 ,2 , -5 , 16 , 17 ,3]))
# print(longestZeroSumSublist([1 ,10, 0 ,0, 27 , 3 , 3 ,1 ]))


                                                                                                            # -242
# L=[-20, -7, -17, -12, 36, 12, -4, -1, -20, 89, -84, 84, -21, -92, -52, -22, -76, 27, 92, -84, -36, -22, -12,  
#     56, 16, -85,-94, -39, -11, 0, -66, 71, 67, -85, 13, 95, 37, -119, -8, -2,   19, -44,  99,  31, -79,  21]
# print(longestZeroSumSubList(L))     #----> False result :  [67, -85, 13, 95, 37, -119, -8]
 # Expected [-39, -11, 0, -66, 71, 67, -85, 13, 95, 37, -119, -8, -2, 19, -44, 99, 31, -79, 21])
# print(len(L))
# print(sum(L[:27]))
# print(sum(L))

