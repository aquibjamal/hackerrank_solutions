#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:49:43 2019

@author: aquib
"""

if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    score_set=set([s[1] for s in students])
    #sort scores set
    score_sorted=sorted(score_set)

    second_name=[]
    for s in students:
        if s[1]==score_sorted[1]:
            second_name.append(s[0])
    #sort students with same second lowest score
    second_name.sort()
    for s in second_name:
        print(s)
    print(end='')
