# -*- coding: utf-8 -*-

from skimage.transform import resize
import math
import numpy as np

def redim(I,size):
    #size is number of pixels of the new picture
    l = I.shape[0]
    h = I.shape[1]
    r = h/l
    if (I.ndim == 3) :
        A = (size)/3 
    else :
        A = size
        
    L = int(math.sqrt(A/r))
    H = int(A/L)
    
    J = resize(I,(L,H))
    J = 255*J
    return J.astype(np.uint8)