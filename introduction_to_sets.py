#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:29:31 2019

@author: aquib
"""

def average(array):
    # your code goes here
    aset=set(array)
    total=sum(aset)
    avg=float(total)/len(aset)
    return avg
