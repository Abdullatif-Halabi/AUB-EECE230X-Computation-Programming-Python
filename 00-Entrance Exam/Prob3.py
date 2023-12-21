# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 15:00:43 2023

@author: abbou
"""

n = str(int(input("Input = ")))
end = False   
    
for i in n :
    if i != "3" and  i != "7" :
        print("Output = 0")
        end = True
        break
    
if end == False :
    x = int(n)
    sum = x

    while x > 0:
        sum += x//10
        x = x//10
    
    print("Output = " , sum)    
        
