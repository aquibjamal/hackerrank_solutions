#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:08:49 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
test=int(input())
cond=[]
for _ in range(test):
    numA=int(input())
    setA=set(map(int,input().split()))
    numB=int(input())
    setB=set(map(int,input().split()))
    if all([a in setB for a in setA]):
        cond.append(True)
    else:
        cond.append(False)

for i in range(len(cond)):
    print(cond[i],"\n",end='')

