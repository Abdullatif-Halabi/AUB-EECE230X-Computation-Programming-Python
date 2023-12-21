# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 20:44:26 2023

@author: abbou

"""

L = [int(x) for x in input('Enter integers spearated by spaces: ').split()]
n = len(L)

allPos = True
allNeg = True
pos_summ = 0

for x in L:
    if x >= 0:
        allNeg = False
        pos_summ += x
    else:
        allPos = False
         
        
        
maxSum = 0
a = 0
b = 0

if allNeg:
    print('Max-sum =',0)
    
elif allPos:
    print('Max-sum =',pos_summ)
    print('A max-sum subsequence: ')
    for x in L:
        print(x , end = ' ')
    
else:    
    for i in range(n):
        for j in range(i , n):
            summ = 0
            for x in L[i : j+1]:
                summ += x
                if summ > maxSum:
                    maxSum=summ
                    a = i
                    b = j+1

    subseq = L[a : b]  
    print('Max-sum =',maxSum)
    print('A max-sum subsequence: ')
    for x in subseq:
        print(x, end=" ")
    
