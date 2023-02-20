# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:40:41 2022

@author: PC-CatLoaf
"""
import math
import random as rd


n = 5
a = []
for i in range(n) :
    x = [rd.randint(1,1000),rd.randint(1,1000)]
    a.append(x)


def closestPair(p) :
    n = len(p)
    d = math.inf
    for i in range(1,n-1):
        for j in range(i+1 , n):
            d = min(d,math.sqrt( ((p[i][0] - p[j][0])**2) + ((p[i][1] - p[j][1])**2)) )
    return abs(d)

print(closestPair(a))
