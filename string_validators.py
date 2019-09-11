#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:23:14 2019

@author: aquib
"""

if __name__ == '__main__':
    s = input()
    print(any([c.isalnum() for c in s]))
    print(any([c.isalpha() for c in s]))
    print(any([c.isdigit() for c in s]))
    print(any([c.islower() for c in s]))
    print(any([c.isupper() for c in s]))

