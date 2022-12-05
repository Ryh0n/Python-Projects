# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:23:19 2020

@author: ryans
"""

import numpy as np
from matplotlib import pyplot as plt

#unpack reads in column format as opposed to default row format

height, weight = np.loadtxt("anthropometry.dat", unpack = True, delimiter = "," \
           ,dtype = float, usecols = (2,3))

gender = np.loadtxt("anthropometry.dat", unpack = True, delimiter = "," \
           ,dtype = str, usecols = (0))
    
handed = np.loadtxt("anthropometry.dat", unpack = True, delimiter = "," \
           ,dtype = str, usecols = (4))

height = height * 2.54
weight = weight / 2.2
heightm = []
weightm = []
heightf = []
weightf = []
n = np.size(height)

for i in np.arange(n):
    if gender[i] == "M":
        heightm = np.append(heightm, height[i])
        weightm = np.append(weightm, weight[i])
    elif gender[i] == "F":
        heightf = np.append(heightf, height[i])
        weightf = np.append(weightf, weight[i])


plt.plot(heightm, weightm, color = "red", marker = "o", markersize = "1", linestyle = "")
plt.plot(heightf, weightf, color = "blue", marker = "o", markersize = "1", linestyle = "")
plt.show()
