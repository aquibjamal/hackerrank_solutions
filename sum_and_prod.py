#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:20:28 2019

@author: aquib
"""

import numpy
N,M=map(int, input().split())
x=numpy.array([input().split() for i in range(N)],int)
sum=numpy.sum(x, 0)
prod=numpy.prod(sum)
print(prod)


