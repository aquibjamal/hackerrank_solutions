#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:22:48 2019

@author: aquib
"""

import numpy
n=list(map(float,input().split()))
m=input()
print(numpy.polyval(n,int(m)))


