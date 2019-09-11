#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:12:23 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

valid_structure = r"[456]\d{3}(-?\d{4}){3}$"
no_four_repeats = r"((\d)-?(?!(-?\2){3})){16}"
filters=valid_structure, no_four_repeats
output=[]
num_cc=int(input())
for _ in range(num_cc):
    cc=input()
    if all(re.match(f, cc) for f in filters):
        output.append("Valid")
    else:
        output.append("Invalid")
for o in output:
    print(o)
