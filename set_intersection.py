#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:53:31 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
#num of English subscribers
num_e=int(input())
roll_e=set(map(int,input().split()))
num_f=int(input())
roll_f=set(map(int,input().split()))
inter=roll_e & roll_f
print(len(inter),end='')
