#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:26:41 2019

@author: aquib
"""



def arrays(arr):
    # complete this function
    # use numpy.array
    l=len(arr)
    x=numpy.zeros(l)
    for i in range(l):
        x[i]=float(arr[l-1-i])
    return x


