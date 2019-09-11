#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:10:20 2019

@author: aquib
"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        number_of_line=len(data.split('\n'))
        if number_of_line >1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        if data.strip():
            print(data)

    def handle_data(self,data):
        if data.strip():
            print(">>> Data")
            print(data)
  
parser=MyHTMLParser
n=int(input())
  
html = ""       
for i in range(n):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

