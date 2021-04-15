# -*- coding: utf-8 -*-

def byte_count(image):

    A = 1
    for i in range (image.ndim) :
        A *= image.shape[i]
    return A  