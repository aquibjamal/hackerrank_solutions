#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:51:42 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
#number of stamps
N=int(input())
stamps=set('')
#read in stamp names
for _ in range(N):
    stamps.add(input())
print(len(stamps),end='')

