#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:24:44 2019

@author: aquib
"""

import numpy
numpy.set_printoptions(legacy='1.13')
N,M=map(int,input().split())
print(numpy.eye(N,M))

