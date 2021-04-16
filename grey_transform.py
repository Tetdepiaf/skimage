# -*- coding: utf-8 -*-

import numpy as np

def grey_transform(I):

    r = [0.2125,0.7154,0.0721]
    J = np.zeros((I.shape[0],I.shape[1]))
    for i in range(3) :
        for j in range(I.shape[0]) :
            for k in range(I.shape[1]) :
                J[j,k] += I[j,k,i]*r[i]
    J = J/J.max()            
    J = 255*J
    return J.astype(np.uint8)