# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:17:07 2022

@author: PC-Pastacat
"""

def a(n):
    if n == 0 :
        return 2
    else :
        return a(n-1) + 2

print(a(8))