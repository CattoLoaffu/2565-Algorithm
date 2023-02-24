# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:13:17 2022

@author: PC-Pastacat
"""

def decAndCon(a,n) :
    if n == 0:
        return 1
    elif n % 2 == 0 :
        return decAndCon(a, n/2)**2
    else :
        return decAndCon(a,(n-1)/2)**2*a
    

print(decAndCon(2, 8))