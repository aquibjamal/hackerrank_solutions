#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:21:09 2019

@author: aquib
"""

def swap_case(s):
    x=[]
    for c in s:
        if c.isalpha():
            c=c.swapcase()
        x.append(c)
    
    return ''.join(x)

