#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:16:46 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
b=int(input())
rem=a//b
mod=a%b
print(rem)
print(mod)
print("(%d, %d)"%(rem,mod),end='')
