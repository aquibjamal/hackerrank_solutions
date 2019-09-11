#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:40:10 2019

@author: aquib
"""

def merge_the_tools(string, k):
    # your code goes here
    l=len(string)
    for i in range(0,l,k):
        s=""
        for j in string[i:i+k]:
            if j in s:
                continue
            else:
                s = s+j
        print(s)

