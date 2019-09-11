#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:29:57 2019

@author: aquib
"""

import numpy
numpy.set_printoptions(sign=' ')
a=input().split()
x=numpy.array(a,dtype=float)
print(numpy.floor(x))
print(numpy.ceil(x))
print(numpy.rint(x))
