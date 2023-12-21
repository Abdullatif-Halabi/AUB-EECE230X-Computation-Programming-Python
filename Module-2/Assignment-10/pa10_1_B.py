def genBinStr2(n, w , dict={}):
    if n < 0 or w < 0:
        return []
    if n == 0:
        if w == 0:
            return ['']
        else:
            return []
    if n == w:
        return ['1' * n]
    
    if (n,w) in dict :
        return dict[(n,w)]

    with_zero = ['0' + s for s in genBinStr2(n - 1, w)]
    with_one = ['1' + s for s in genBinStr2(n - 1, w - 1)]

    dict[(n,w)] = with_zero + with_one
    
    return dict[(n,w)]


# print(genBinStr2(3, 0)) 
# print(genBinStr2(3, 1))  
# print(genBinStr2(3, 2))  
# print(genBinStr2(3, 3))  
# print(genBinStr2(4, 2))  
# print(genBinStr2(6, 1))  