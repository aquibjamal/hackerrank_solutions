#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:31:11 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
numa=int(input())
seta=set(map(int,input().split()))
numb=int(input())
setb=set(map(int,input().split()))
u=seta.union(setb)
i=seta.intersection(setb)
ai=u-i
ai=sorted(ai)
for i in ai:
    print(i)
