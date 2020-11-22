# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:14:46 2020

@author: edwil
"""

import matplotlib.pyplot as plt
 
x = [5,10,20,40,80,120,160]
y1 = [21.5675,22.0287,21.8787,20.9987,20.2512,20.3062,20.4587]
y2 = [18.6237,21.4599,23.5275,24.3125,24.1512,23.6037,23.1175]
plt.plot(x, y2,label='user')
plt.plot(x, y1,label='item')
plt.title('Precision')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()



x = [5,10,20,40,80,120,160]
y1 = [16.0787,16.4225,16.3125,15.6575,15.1012,15.1412,15.2562]
y2 = [13.8875,15.9987,17.5425,18.1262, 18.0062,17.5999,17.2362]
plt.plot(x, y2,label='user')
plt.plot(x, y1,label='item')
plt.title('Recall')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()



x = [5,10,20,40,80,120,160]
y1 = [20.5550,15.9962,13.0162,11.7075,11.1225,11.2725, 11.7450]
y2 = [39.4387,30.9825,23.7324,18.0962,14.1075, 12.3150,11.1749]
plt.plot(x, y2,label='user')
plt.plot(x, y1,label='item')
plt.title('Coverage')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()