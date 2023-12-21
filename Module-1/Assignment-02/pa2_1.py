# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 19:51:57 2023

@author: abbou
"""
print("Let's calculate the factorial of a number 'n' !")
n = int(input("Enter an integer n : "))

if n<0 :
    print("Negative number !")
    
elif n==0 :
    fac = 1
    print("Factorial of n: " , fac)
    
else :
    fac = 1
    for i in range(1,n+1):
        fac *= i
    print("Factorial of n: " , fac)
    