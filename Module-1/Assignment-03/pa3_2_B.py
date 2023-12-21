# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 18:55:59 2023

@author: abbou
"""

L1 = [ int(x) for x in input('Enter the integers \
in the first sequence spearated by spaces:').split()]
    
L2 = [ int(x) for x in input('Enter the integers\
in the second sequence spearated by spaces:').split() ]

identical = True 

if L2 != L1 :
    identical = False
    
if identical :
    print('Sequences are equal')   
else:
    print('Sequences are not equal')