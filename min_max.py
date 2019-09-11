#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:21:03 2019

@author: aquib
"""

import numpy
N,M=map(int,input().split())
x=numpy.array([input().split() for _ in range(N)], int)
mn=numpy.min(x,1)
mx=numpy.max(mn)
print(mx)
