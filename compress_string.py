#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:41:01 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

print(*[(len(list(c)), int(k)) for k,c in groupby(input())])
