#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:32:10 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
number=complex(input().strip())
print("%.3f"%cmath.polar(number)[0])
print("%.3f"%cmath.polar(number)[1])
