#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:37:13 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

N,X=map(int,input().split())
s=[]

for _ in range(X):
    s.append(map(float,input().split()))

for i in zip(*s):
    print(sum(i)/len(i))
