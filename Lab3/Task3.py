# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:27:04 2022

@author: PC-CatLoaf
"""
import random as rd

def randomChar(n) :
    namex = ""
    for i in range(n):
        namex = namex + chr(rd.randint(97,100))
    
    return namex


def matchBFS(t,p):
    n = len(t)
    m = len(p)
    for i in range(n-m) :
        j = 0
        while j < m and p[j] == t[i+j] :
            j = j+1
        if j == m :
            return "found at index " + str(i)
    return "Not found"


pattern = randomChar(3)
text = randomChar(200)
print(pattern)
print(text)
print(matchBFS(text, pattern))