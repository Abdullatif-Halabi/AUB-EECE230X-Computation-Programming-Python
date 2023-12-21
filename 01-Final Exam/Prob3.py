def pattern(k):
    assert k>=0 , 'Bad Input!'
    if k in (0,1) :
        return '1'
    else:
        return (pattern(k-1)+ '0'*k + pattern(k-2))
    

# for k in range(0,6):
#     print("pattern("+str(k)+"): " + pattern(k))
    