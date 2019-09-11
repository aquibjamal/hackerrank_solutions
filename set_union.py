#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:52:43 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
#read in number of English subscribers
num_e=int(input())
#read roll number of English subscribers
roll_e=list(map(int, input().split()))

#read in number of French subscribers
num_f=int(input())
#read roll number of French subscribers
roll_f=list(map(int,input().split()))

total=roll_e+roll_f
print(len(set(total)),end='')
