#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:31:26 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB=float(input())
BC=float(input())

print(str(int(round(math.degrees(math.atan2(AB,BC))))) + '°')
