#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:29:43 2019

@author: aquib
"""

import numpy
N,M=map(int,input().split())
a,b=(numpy.array([input().split() for _ in range(N)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')
