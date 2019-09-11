#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:25:35 2019

@author: aquib
"""

import numpy
numpy.set_printoptions(legacy='1.13')
n,m,p=map(int,input().split())
a=numpy.array([(input().split()) for _ in range(n)], int)
b=numpy.array([(input().split()) for _ in range(m)], int)
print(numpy.concatenate((a,b),axis=0))