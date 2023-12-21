def merge(L , R):
    if not L or not R :
        C = L + R
    elif L[-1] <= R[0] :
        C = L + R
    elif R[-1] <= L[0] :
        C = R + L
    else :
        C = []
        i = j = 0
        r = len(R)
        l = len(L)
        while i < r and j < l :
            if R[i] < L[j] :
                C.append(R[i])
                i += 1
            elif R[i] > L[j] :
                C.append(L[j])
                j += 1
            else :
                C.append(R[i])
                C.append(L[j])
                i += 1
                j += 1
                
            if i == r or j == l:
                C.extend(R[i:])
                C.extend(L[j:])
                break
    return C


# print(merge(L = [-4, -4, 7, 8, 11, 19, 19, 26, 31, 33, 35, 36, 41, 42, 43, 49, 51, 56, 61, 64, 91],R = [20, 21, 23, 25, 44, 55, 58, 59, 62, 63, 67, 72, 74, 83, 88, 95, 96]))
# print(merge([1,5,7],[2,3,5,8,9,9]))
# print(merge([1,5,7],[20,30,50,80,90,90]))
print(merge([10,50,70],[2,3,5,8,9,9]))
# print(merge([1,5,7],[]))
# print(merge([],[2,3,5,8,9,9]))
# print(merge([1,2,3],[1,2,3]))