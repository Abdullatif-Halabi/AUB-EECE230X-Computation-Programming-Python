# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:46:00 2023

@author: abbou
"""

n = int(input('Enter the number of integers : '))
isSorted = True

x1 = int(input('Enter an integer : '))
for i in range(n-1):
    x = int(input('Enter an integer : '))
    if x - x1 < 0:
        isSorted = False
        break
    x1 = x
    
if isSorted :
    print('YES: input is sorted')
else:
    print('NO: input is not sorted')