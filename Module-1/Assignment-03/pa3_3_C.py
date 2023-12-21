# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 14:47:07 2023

@author: abbou
"""


L = [int(x) for x in input('Enter integers spearated by spaces: ').split()]
n = len(L)

allPos = True
allNeg = True

for x in L:
    if x >= 0:
        allNeg = False
    else:
        allPos = False
         
        
        
maxSum = 0
a = 0
b = 0

if allNeg:
    print('Max-sum =',0)
    
elif allPos:
    print('Max-sum =',sum(L))
    print('A max-sum subsequence: ')
    for x in L:
        print(x , end = ' ')
        
else:    
    for i in range(n):
        summ = 0
        for j in range(i , n):
            summ += L[j]
            if summ > maxSum:
                maxSum=summ
                a = i
                b = j+1

    # subseq = L[a : b]  
    print('Max-sum =',maxSum)
    print('A max-sum subsequence: ')
    for i in range(a , b):
        print(L[i], end=" ")