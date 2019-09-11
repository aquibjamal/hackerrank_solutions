#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:43:50 2019

@author: aquib
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = [list(map(int, input().split())) for i in range(n)]
    k = int(input())

    nums.sort(key=lambda x: x[k])

    for line in nums:
        print(*line, sep=' ')
