# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:30:44 2023

@author: abbou
"""

n = int(input("Enter n : "))

if n <= 0 :
    print("Empty sequence")
    
else :
    for i in range(n):
        if (i == 0) or (i%2 == 0) :
            print(n , end=" ")
            
        if i%2 != 0 :
            print(n-1 , end=" ")

    
    