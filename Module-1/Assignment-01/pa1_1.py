# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 03:07:28 2023

@author: abbou
"""
from math import ceil

fd = abs(int(input("Enter the price of all the purchased food:")))
dr = abs(int(input("Enter the price of all the purchased drinks:")))
ppl= abs(int(input("Enter number of people :")))

tot =fd + dr + ppl
tip = tot*15/100
total= tot + tip


share= ceil(total/ppl)

print("share = ", share , "pounds")
