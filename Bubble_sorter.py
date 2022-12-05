# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:06:29 2021

@author: ryans
"""
from matplotlib import pyplot as plt
from random import randint

listt = []
Q = int(input('How long do you want your list to be? '))
listcount = 1
while listcount <= Q:
    listt.append(randint(0,1000))
    listcount += 1

print ('Your list:',listt)
counter = 0
plt.figure(2)
plt.plot(listt, color = "red", marker = "o", markersize = 1, linestyle = "")
while counter < Q:
    n = 1
    while Q-counter > n:
        if listt[n-1] > listt[n]:
            listt[n-1], listt[n] = listt[n], listt[n-1]
            n += 1
        else:
            n += 1
    counter += 1
    
print ('Your sorted list:',listt)
plt.figure(1)
plt.plot(listt, color = "red", marker = "o", markersize = 0.3, linestyle = "")