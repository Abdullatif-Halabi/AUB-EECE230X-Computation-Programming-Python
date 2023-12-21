# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:39:52 2023

@author: abbou
"""

cand = int(input("Enter number of candies : "))
stud = int(input("Enter number of students : "))
max_share = 0

if cand <= 0 or stud <= 0 :
    print("Your inputs should be greater than zero")
    
else:
    
    for i in range(1 , cand+1):
        if i * stud <= cand:
            max_share += 1
            
        else:
            break
        
    remain = cand - max_share*stud
        
    print("Number of remaining candies : ", remain)