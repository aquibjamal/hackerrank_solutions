#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:28:36 2019

@author: aquib
"""

cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a=[0,1]
    for i in range(2,n):
        a.append(a[i-2]+a[i-1])
    return a[0:n]
