#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:42:05 2019

@author: aquib
"""

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    x=[str(i) for i in range(1,n+1)]
    y=int(''.join(x))
    print(y)
