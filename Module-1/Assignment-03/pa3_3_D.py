# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 15:04:44 2023

@author: abbou
"""


L = [int(x) for x in input('Enter integers separated by spaces: ').split()]
n = len(L)

if n == 0:
    print('Max-sum = 0')
else:
    summ = maxSum = L[0]
    position = 0
    a = b = 0
    
    for i in range(1, n):
        if L[i] > summ + L[i]:
            summ = L[i]
            position = i
        else:
            summ += L[i]

        if summ > maxSum:
            maxSum = summ
            a = position
            b = i

    if maxSum < 0:
        print('Max-sum = 0')
    else:
        print('Max-sum =', maxSum)
        print('A max-sum subsequence:')
        for i in range(a, b + 1):
            print(L[i], end=" ")

