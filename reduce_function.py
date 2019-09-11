#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:41:58 2019

@author: aquib
"""



import operator

def product(fracs):
    t = reduce(operator.mul, fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator

