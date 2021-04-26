# -*- coding: utf-8 -*-

import numpy as np
import skimage

def fma(J, S=5):
    k = int(S/2)   
    n = J.shape[0]
    m = J.shape[1]
    
    R = np.zeros((n,m))
    selem = np.ones((S,S))
    a = skimage.filters.rank.maximum(J,selem)
    b = skimage.filters.rank.minimum(J,selem)
    c = skimage.filters.rank.median(J,selem)
    
    for i in range(k,n):
        for j in range(k,m):
            if(J[i,j] == a[i,j] or J[i,j] == b[i,j]):
                R[i,j] = c[i,j]
            else :
                R[i,j] = J[i,j]
                 
    return R.astype(np.uint8)

def ratio_eqm(I, J, S=5):
    
    selem = np.ones((S,S))
    K = skimage.filters.median(J, selem)
    L = fma(J,S)

    eqmfma = skimage.metrics.mean_squared_error(I, L)
    eqmmed = skimage.metrics.mean_squared_error(I, K)
    r = eqmfma/eqmmed

    return r