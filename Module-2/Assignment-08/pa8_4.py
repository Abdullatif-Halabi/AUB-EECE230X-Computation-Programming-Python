# def merge_three(L , C, R):
#     D = []
#     m ,n , o = len(L) , len(R) , len(C)
#     i, j, k = 0, 0,0
    
#     while i!=m and j!=n and k!=o :
#         if L[i]<=R[j] and L[i]<=C[k]:
#             D.append(L[i])
#             i+=1
#         elif C[k]<=L[i] and C[k]<=R[j]:
#             D.append(C[k])
#             k +=1
#         else:
#             D.append(R[j])
#             j+=1

#     if i==m :
#             A = merge(C[k:] , R[j:])
#     if  k==o :
#             A = merge(L[i:] , R[j:])
#     if j==n :
#             A = merge(C[k:] , L[i:])

#     return D+A


def merge(L , R):
    C = []
    m = len(L)
    n = len(R)
    i = 0
    j = 0 
    while i!=m and j !=n :
        if L[i]<R[j]:
            C.append(L[i])
            i+=1
        else:
            C.append(R[j])
            j+=1
    while i!=m:
        C.append(L[i])
        i+=1
    while j!=n:
        C.append(R[j])
        j+=1
    return C


def ternaryMergeSort(A,low,high):
    if low < high :
        third = low + (high-low)//3
        twoThird = low + 2*(high-low)//3
        ternaryMergeSort(A,low,third)
        ternaryMergeSort(A,third+1,twoThird)
        ternaryMergeSort(A,twoThird+1,high)

        A[low:high+1] = merge(merge(A[low:third+1] , A[third+1 : twoThird+1])  ,A[twoThird+1:high+1] )





# B = [-8 , -10 , 7 , 9 , 4 , 1 , -9 , 0 , 33]
# print(ternaryMergeSort(B , 0 , len(B)-1))

# C = [12, -3, -16, 5, -3, 17, -11, 7, 2, -1, 20, 11, 5, 16, 4, 11, 0, -13, -7, -9, 15, 18, 6, 19, -17, 18, -1, 1, 1, -5, 14, -13, 14, 20, -7, -17, -12, -11, 3, -6, -17, 13, 15, -3, -4, 18, 5, -18, -8, -3, 14, 5, 15, 18, 15, -11, -4, 20]
# A = [12, -3, -16, 5, -3, 17, -11, 7, 2, -1, 20, 11, 5, 16, 4, 11, 0, -13, -7, -9, 15, 18, 6, 19, -17, 18, -1, 1, 1, -5, 14, -13, 14, 20, -7, -17, -12, -11, 3, -6, -17, 13, 15, -3, -4, 18, 5, -18, -8, -3, 14, 5, 15, 18, 15, -11, -4, 20]
# A.sort()
# print(A==ternaryMergeSort(C,0,len(C)-1))

# # R = [19, -20, -8, 18, -19, 16]
# # print(ternaryMergeSort(C , 0 , len(C)-1))


# import time
# start_time = time.time()
# C = [18, -18, -8, -14, 16, 10, -7, -18, 4, 15, 0, -13, 14, -20, -10, 5, -1, 17, 11, -7, -5, 3, -1, 4, -16, -12, 14, -4, -12, 15, -3, -11, 18, 11, 12, -18, 18, 9, -5, 9, -5, 5, -20, 14, 12, -1, -18, 13, 0, 4, 20, 0, -1, -15, 17, -12, -19, 5, 13, 1, 20, 1, 2, 3, -6, -1, -16, -18, 1, -20, 5, -5, -13, -13, -8, 12, -7, -18, -17, -7, -13, 20, -6, 8, -1, -1, 7, 4, -18, 4, 9]
# ternaryMergeSort(C , 0 , len(C)-1)
# print(C)
# # A = [20-i for i in range(20)]
# # print(ternaryMergeSort(A , 0 , len(A)-1))
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Time taken: {elapsed_time} seconds")


