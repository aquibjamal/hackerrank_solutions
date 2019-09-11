#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:11:29 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

num_input=int(input())
for _ in range(num_input):
    UID=''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', UID)
        assert re.search(r'\d\d\d',UID)
        assert not re.search(r'[^a-zA-Z0-9]',UID)
        assert not re.search(r'(.)\1',UID)
        assert len(UID)==10
    except:
        print('Invalid\n',end='')
    else:
        print('Valid\n',end='')
