# -*- coding: utf-8 -*-

import skimage
from  scipy.signal import convolve2d
import numpy as np

def DoG(I, sigma=1, k=2):
    J = skimage.filters.gaussian(I,k*sigma) - skimage.filters.gaussian(I,sigma)
    return J

def kernel_log(sigma=1, radius_size=1):
    k = radius_size
    x = np.arange(-k,k+1)
    [i,j] = np.meshgrid(x,x)
    h = -(1/(np.pi*sigma**4)) * (1-((i**2+j**2)/(2*sigma**2))) * np.exp(-(i**2+j**2)/(2*sigma**2))
    h = h/np.sum(h)
    return h

def LoG(I, sigma=3, radius_size=15):
    h = kernel_log(sigma=3,radius_size=15)
    J = convolve2d(I,h,mode='same',boundary='fill')
    return J