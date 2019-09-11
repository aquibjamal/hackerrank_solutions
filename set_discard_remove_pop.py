#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:52:22 2019

@author: aquib
"""

n = int(input())
s = set(map(int, input().split()))
num_ops=int(input())
for _ in range(num_ops):
    command=input().split()

    if command[0] == 'pop':
        s.pop()
    elif command[0]== 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))
print(sum(s),end='')

