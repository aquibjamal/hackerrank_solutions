#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:19:08 2019

@author: aquib
"""

import string

def print_rangoli(size):
    # your code goes here
    alpha=string.ascii_lowercase
    n=size
    L=[]
    for i in range(n):
        s="-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3,"-"))
    print('\n'.join(L[:0:-1]+L))
