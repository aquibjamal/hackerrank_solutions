#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:54:55 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_A=int(input())
A=set(map(int,input().split()))
num_ops=int(input())
for _ in range(num_ops):
    c=input().split()
    command=c[0]
    num_B=c[1]
    B=set(map(int,input().split()))
    if command=='intersection_update':
        A.intersection_update(B)
    if command=='update':
        A.update(B)
    if command=='symmetric_difference_update':
        A.symmetric_difference_update(B)
    if command=='difference_update':
        A.difference_update(B)
print(sum(A),end='')        

