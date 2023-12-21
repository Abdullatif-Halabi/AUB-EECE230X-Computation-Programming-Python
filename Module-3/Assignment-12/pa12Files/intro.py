# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:09:55 2018

@author: louay
"""


from graph import buildGraphFromFile 
import matplotlib.pyplot as plt
G = buildGraphFromFile("DiGraph1.txt", undirected = False)
plt.figure(1)
plt.clf()
G.draw()
plt.show()

G = buildGraphFromFile("UndirectedGraph1.txt", undirected = True)
plt.figure(2)
plt.clf()
G.draw()