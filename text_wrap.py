#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:25:34 2019

@author: aquib
"""



def wrap(string, max_width):
    return '\n'.join([string[i:i+max_width] for i in range(0,len(string), max_width)])

