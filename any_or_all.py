#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:44:28 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
nums = list(map(int, input().split()))
cond1=all([i>0 for i in nums])
cond2=any([str(i)==str(i)[::-1] for i in nums])
print(cond1 and cond2)
