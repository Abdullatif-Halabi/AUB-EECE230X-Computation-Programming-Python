# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 23:31:20 2023

@author: abbou
"""

n = int(input("Enter the number of integers u'll provide : "))

if n<0 :
    print("n should be a natural number")
    
elif n==0 :
    print("Empty sequence.")

else :
    
    max=0
    
    for i in range(n):
        x=int(input("enter the integer : "))
        if x>=max:
            max=x
            
    print("the biggest number is : ", max)           
        