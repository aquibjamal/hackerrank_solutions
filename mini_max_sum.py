#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:35:50 2019

@author: aquib
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max_list=[]
    min_list=[]

    l=arr.copy()
    for j in range(4):
        mx=max(l)
        max_list.append(mx)
        l.remove(mx)
    
    x=arr.copy()
    for j in range(4):
        mn=min(x)
        min_list.append(mn)
        x.remove(mn)

    print(sum(min_list),sum(max_list))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
