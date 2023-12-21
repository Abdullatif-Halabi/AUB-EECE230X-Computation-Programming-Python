def concatenateHorizontal(A, B):
    if not A:
        return []
    else:
        row = A[0] + B[0]
        return [row] + concatenateHorizontal(A[1:], B[1:])
    

def generatePattern(k) :
    if k==0: return [[1]]

    combine = (generatePattern(k-1))
    upperPart = concatenateHorizontal(combine,combine)
    lowerPart = concatenateHorizontal([[0 for i in range(2**(k-1))] for j in range(2**(k-1))],combine)


    return upperPart+lowerPart




import numpy
for k in range(5):
    print("k=",k,":")
    print(numpy.matrix(generatePattern(k)),"\n")
# For fun: show matrix as a figure with 1 and 0 in different colors
import matplotlib.pyplot as plt
plt.imshow(generatePattern(10))
plt.show()
