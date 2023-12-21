def recPowerFast(x,n):
    # global N
    # N += 1
    assert int(n) == n  , "the exponent should be an integer"
    if n == 0:
        return 1
    elif n < 0:
        x = 1 / x
        n = -n

    if n % 2 == 0:
        half_pow = recPowerFast(x, n // 2)
        return half_pow * half_pow
    else:
        half_pow = recPowerFast(x, (n - 1) // 2)
        return x * half_pow * half_pow


'''The recurrence is when the exponent is an even number bigger than 2 , we know that we can keep divide it by 2 and multiply the whole
new number by itself to get the original number '''




# N = 0     
# print("recPowerFast(0,0):",recPowerFast(0,0))
# print("recPowerFast(0,3):",recPowerFast(0,3))
# print("recPowerFast(3,0):",recPowerFast(3,0))
# print("recPowerFast(3,1):",recPowerFast(3,1))
# print("recPowerFast(-3,1):",recPowerFast(-3,1))
# print("recPowerFast(2,4):",recPowerFast(2,4))
# print("recPowerFast(2,-4):",recPowerFast(2,-4))
# x = 1.25
# n = 82
# print(x,"**",n," :",x**n)
# print("recPower(",x,",",n,"):",recPowerFast(x,n))
# print("N : " , N)