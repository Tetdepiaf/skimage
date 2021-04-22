# -*- coding: utf-8 -*-

import numpy as np

def ajustement_gamma(I, gamma=2):
    n = I.shape[0]
    m = I.shape[1]
    I2 = np.zeros((n,m))
    
    for i in range(n):
        for j in range(m):
            I2[i,j] = I[i,j]**gamma
    I2 = 255*I2/np.max(I2)
    
    return I2.astype(np.uint8)