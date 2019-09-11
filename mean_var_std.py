#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:21:26 2019

@author: aquib
"""

import numpy
numpy.set_printoptions(legacy='1.13')

N,M=map(int, input().split())
x=numpy.array([input().split() for i in range(N)], int)
mean=numpy.mean(x,1)
var=numpy.var(x,0)
std=numpy.std(x)
print(mean)
print(var)
print(std)

