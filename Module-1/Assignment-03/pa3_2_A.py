# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 18:02:14 2023

@author: abbou
"""

L1 = [ int(x) for x in input('Enter the integers \
in the first sequence spearated by spaces:').split()]
    
L2 = [ int(x) for x in input('Enter the integers\
in the second sequence spearated by spaces:').split() ]
    
identical = True

  
if len(L1) != len(L2) :
    identical = False

else :
    for i in range(len(L1)):
        if L1[i] != L2[i] :
            identical = False
            
    
if identical:
    print('Sequences are equal')
    
else:
    print('Sequences are not equal') 
      
    