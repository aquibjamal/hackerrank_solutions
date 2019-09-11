#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:48:31 2019

@author: aquib
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x=sorted(arr)
    second_largest_index=x.count(max(x))
    y=x[:-second_largest_index]
    print(y[-1])
