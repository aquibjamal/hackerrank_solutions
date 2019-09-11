#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:41:35 2019

@author: aquib
"""

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        leap=True
        if year%100==0:
            leap=False
        if year%400==0:
            leap=True
    return leap

