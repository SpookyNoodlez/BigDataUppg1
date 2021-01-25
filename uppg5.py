# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 01:13:50 2021

@author: joann
"""

import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
b = a.reshape(-1,1)

c = np.multiply(a,b)

print(c)