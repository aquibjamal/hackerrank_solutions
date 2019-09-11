#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:43:22 2019

@author: aquib
"""



def print_from_stream(n, stream=None):
    if stream is None:
        stream=EvenStream()
    for _ in range(n):
        print(stream.get_next())

