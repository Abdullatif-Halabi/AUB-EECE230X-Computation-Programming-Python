import numpy

def concatenateHorizontal(A, B):
    if not A:
        return []
    else:
        row = A[0] + B[0]
        return [row] + concatenateHorizontal(A[1:], B[1:])





# A = [[1, 2, 3], [4, 5, 6]]
# B = [[7, 8, 9], [10, 11, 12]]
# C = A + B
# D = concatenateHorizontal(A, B)

# print("A:")
# print(numpy.matrix(A))
# print("\nB:")
# print(numpy.matrix(B))
# print("\nC:")
# print(numpy.matrix(C))
# print("\nD:")
# print(numpy.matrix(D))
