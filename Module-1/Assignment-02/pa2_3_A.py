# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 23:48:29 2023

@author: abbou
"""
#PART A
n = int(input("Enter n:"))
if n <= 1:
    print(n,"is not prime")
else:
    isPrime = True
    d = 2 
    while d**2 <= n:
        
        if n%d == 0 :
            isPrime = False
            break
        d+=1
        
    if isPrime :
        print(n,"is Prime")
        
    else :
        print(n, "is divisible by", d,"\n")
             
    