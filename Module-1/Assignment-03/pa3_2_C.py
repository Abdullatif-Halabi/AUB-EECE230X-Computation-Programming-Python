# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 19:10:45 2023

@author: abbou
"""

L1 = [ int(x) for x in input('Enter the integers \
in the first sequence spearated by spaces:').split()]
    
L2 = [ int(x) for x in input('Enter the integers\
in the second sequence spearated by spaces:').split() ]

# n = len(L1)
permu = True


if len(L1) != len(L2) :
    permu = False
    
else :
    for i in range(len(L1)):
        i =0
        for j in range(len(L2)):
            if L1[i] == L2[j]:
                permu = True
                L1 =L1[i+1:]
                L2 = L2[:j]+L2[j+1:]
                break
            else:
                permu = False
             
            
if permu :
    print('YES: second sequence is a permutation of the first')

else:
    print('NO: second sequence is not a permutation of the first')
        
