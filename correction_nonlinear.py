# -*- coding: utf-8 -*-

import numpy as np
import sys

def ajustement_nonlineaire(I, E=1):
    moy = I.mean()
    eps = sys.float_info.epsilon
    
    n = I.shape[0]
    m = I.shape[1]
    I2 = np.zeros((n,m))
    
    for i in range(n):
        for j in range(m):
            I2[i,j] = 1/(1+(moy/(I[i,j]+eps))**E)
    I2 = 255*I2/np.max(I2)
    
    return I2.astype(np.uint8)