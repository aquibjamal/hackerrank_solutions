#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:28:00 2019

@author: aquib
"""

import numpy
x=input().strip().split(' ')
b=[int(i) for i in x]
a=numpy.array(b)
o=numpy.reshape(a,(3,3))
print(o)