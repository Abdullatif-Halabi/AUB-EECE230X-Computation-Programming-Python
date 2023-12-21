# def genBinStr2(n, w):
#     if n < 0 or w < 0:
#         return []
#     if n == 0:
#         if w == 0:
#             return ['']
#         else:
#             return []

#     X = genBinStr2(n - 1, w)
    
#     with_zero = ['0' + s for s in X]
    
#     if w > 0:
#         with_one = ['1' + s for s in genBinStr2(n - 1, w - 1)]
#     else:
#         with_one = []

#     return with_zero + with_one

def genBinStr2(n, w):
    if n < 0 or w < 0:
        return []
    if n == 0:
        if w == 0:
            return ['']
        else:
            return []
    if n == w:
        return ['1' * n]
    
    with_zero = ['0' + s for s in genBinStr2(n - 1, w)]
    with_one = ['1' + s for s in genBinStr2(n - 1, w - 1)]
    
    return with_zero + with_one

# print(genBinStr2(3, 0)) 
# print(genBinStr2(3, 1))  
# print(genBinStr2(3, 2))  
# print(genBinStr2(3, 3))  
# print(genBinStr2(4, 2))  
# print(genBinStr2(6, 1))  