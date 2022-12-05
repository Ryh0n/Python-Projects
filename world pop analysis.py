# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:23:41 2020

@author: ryans
"""

import numpy as np
from matplotlib import pyplot as plt

year, pop = np.loadtxt("world_pop.dat", unpack = True, delimiter = "," \
           ,dtype = float)

plt.plot(year, pop, marker = "o", markersize = "3", linestyle = "")
plt.show()