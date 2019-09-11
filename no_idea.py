#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:27:15 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
arr=list(map(int,input().split()))
a=set(map(int,input().split()))
b=set(map(int,input().split()))
h=0
for i in arr:
    if i in a:
        h= h+1
    if i in b:
        h=h-1
print(h)
