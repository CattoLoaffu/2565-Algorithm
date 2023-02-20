# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:05:28 2022

@author: PC-CatLoaf
"""
import random as rd

n = 20
a = []
for i in range(n) :
    a.append(rd.randint(1,1000))


def bubbleSort(a) :
    n = len(a)
    for i in range(n-1) :
        for j in range(n-1-i):
            if a[j + 1] < a[j] :
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a

print(a)
print(bubbleSort(a))