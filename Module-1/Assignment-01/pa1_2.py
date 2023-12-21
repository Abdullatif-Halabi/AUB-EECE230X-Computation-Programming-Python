# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 03:42:34 2023

@author: abbou
"""

x = abs(int(input("Enter the number of elapsed seconds: ")))
hr = x//3600
mins = (x-hr*3600)//60
sec = x-hr*3600-mins*60

print("Converted time:  ", hr , ":" , mins , ":" , sec)