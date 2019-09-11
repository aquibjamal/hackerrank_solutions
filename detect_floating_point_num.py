#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:38:25 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$',input())))
