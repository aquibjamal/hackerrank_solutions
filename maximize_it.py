#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:44:11 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k,m=map(int,input().split())
n=(list(map(int, input().split()))[1:] for _ in range(k))
results=map(lambda x:sum(i**2 for i in x)%m, product(*n))
print(max(results))
