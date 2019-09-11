#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:21:53 2019

@author: aquib
"""

import numpy
n=int(input())
a=numpy.array([input().split() for _ in range(n)], int)
b=numpy.array([input().split() for _ in range(n)], int)
m=numpy.dot(a,b)
print(m)
