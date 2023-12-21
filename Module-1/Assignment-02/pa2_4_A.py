# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 00:38:16 2023

@author: abbou
"""
##PART A
n=int(input("Enter an integer n : "))
if n < 0 :
    print(n , "is not a square")

elif n==0 or n==1 :
    print("YES square: " , n , "=" ,n, "^2")
    
else :
    square = False
    
    for d in range(2,n//2):
        if d*d == n:
            square = True
            break

    if square:
        print("YES square: " , n , "=" ,d, "^2")
        
    else:
        print(n,"is not a square")
        
        
        
        
        
        
        