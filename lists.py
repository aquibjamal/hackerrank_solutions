#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:29:04 2019

@author: aquib
"""

if __name__ == '__main__':
    N = int(input())
    l=[]
    for _ in range(N):
        s=input().split()
        command=s[0]
        arg=s[1:]
        if command!="print":
            command = command + "("+",".join(arg)+")"
            eval("l."+command)
        else:
            print(l)
