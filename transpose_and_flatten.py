#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:28:40 2019

@author: aquib
"""

import numpy
row,col = map(int,input().split())
array=[]
for i in range(int(row)):
    x=input().split()
    array.append(x)

lis1=numpy.array(array,int)
print(numpy.transpose(lis1))
print(lis1.flatten())
