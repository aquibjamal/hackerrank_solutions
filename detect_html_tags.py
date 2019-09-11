#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:11:09 2019

@author: aquib
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag,attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]

html='\n'.join([input() for _ in range(int(input()))])
parser=MyHTMLParser()
parser.feed(html)
parser.close()
