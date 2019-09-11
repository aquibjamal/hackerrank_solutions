#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:58:50 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
K=int(input())
rooms=list(map(int,input().split()))
s=set(rooms)
x=(sum(s)*K-sum(rooms))//(K-1)
#since captains room will be included K times in sum(s)*K, divide by K-1
print(x,end='')
