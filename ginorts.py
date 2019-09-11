#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:46:07 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
x=input()
lowchar=[]
uppchar=[]
odddigit=[]
evendigit=[]
for i in x:
    if i.isalpha():
        if i.isupper():
            uppchar.append(i)
        else:
            lowchar.append(i)
    elif i.isdigit():
        if int(i)%2==0:
            evendigit.append(i)
        else:
            odddigit.append(i)
y=''.join(sorted(lowchar)+sorted(uppchar)+sorted(odddigit)+sorted(evendigit))
print(y)
