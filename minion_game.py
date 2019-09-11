#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:40:36 2019

@author: aquib
"""

def minion_game(string):
    # your code goes here
    vowels="AEIOU"

    k=0
    s=0
    l=len(string)
    for i in range(l):
        if string[i] in vowels:
            k = k + l - i
        else:
            s = s + l - i

    if k>s:
        print("Kevin",k)
    elif k<s:
        print("Stuart",s)
    else:
        print("Draw")


