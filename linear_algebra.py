#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:23:58 2019

@author: aquib
"""

import numpy
numpy.set_printoptions(legacy='1.13')
N=int(input())
x=numpy.array([input().split() for i in range(N)], float)
print(numpy.linalg.det(x))