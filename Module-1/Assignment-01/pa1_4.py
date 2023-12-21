# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 04:38:20 2023

@author: abbou
"""

a = float(input("Enter a (non-zero number) : "))
b = float(input("Enter b : "))
c = float(input("Enter c : "))



if a==0 :
    print(" 'a' should be different than zero")

else:
    dis = b**2 - 4*a*c
    
    if dis>10e-9 :
        x1 = (-b+dis**0.5)/(2*a)
        x2 = (-b-dis**0.5)/(2*a)
        print("the equation has two distinct roots: ", x1 , "and" , x2)
        
    elif abs(dis) <= 10e-9   :
        x = -b/(2*a)
        print("the equation has one root: ", x)
        
    else:
        print("The equation has no  roots.")
    
