# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:15:37 2023

@author: abbou
"""

L = [int(x) for x in input('Enter integers spearated by spaces:').split()]
n = len(L)
isSorted = True

for i in range(n-1):
    if L[i+1] < L[i]:
        isSorted = False
        break

if isSorted:
    print('YES: input is sorted')
else:
    print('NO: input is not sorted')