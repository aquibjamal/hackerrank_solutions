#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:22:23 2019

@author: aquib
"""

import numpy
numpy.set_printoptions(legacy='1.13')
a=numpy.array([input().split()], int)
b=numpy.array([input().split()], int)
print(numpy.asscalar(numpy.inner(a,b)))
print(numpy.outer(a,b))


