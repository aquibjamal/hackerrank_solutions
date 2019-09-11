#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:09:07 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
setA=set(map(int,input().split()))
cond=[]
numB=int(input())
for _ in range(numB):
    setB=set(map(int,input().split()))
    cond1=all([b in setA for b in setB])
    cond2=len(setA)>len(setB)
    cond.append(cond1 and cond2)

print(all(cond),end='')
