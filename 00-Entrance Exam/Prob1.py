# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:06:18 2023

@author: abbou
"""
x1 = float(input("Enter price of 1 kg tomatoes in near supermarket:"))
y1 = float(input("Enter price of 1 bunch of Parsley in near supermarket:"))
z1 = float(input("Enter price of 1 kg bulgur in near supermarket:"))

x2 = float(input("Enter price of 1 kg tomatoes in far supermarket:"))
y2 = float(input("Enter price of 1 bunch of Parsley in far supermarket:"))
z2 = float(input("Enter price of 1 kg bulgur in far supermarket:"))

destiny = "Near"

if (3*x2 + 4*y2 <= 0.7 * (3*x1 + 4*y1)) or (3*x2 + 0.5*z2 <= 0.7 * (3*x1 + 0.5*z1))  or (4*y2 + 0.5*z2 <= 0.7 * (4*y1 + 0.5*z1)) :
    destiny = "Far"
    
print(destiny)