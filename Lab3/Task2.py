# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:16:00 2022

@author: PC-CatLoaf
"""
import random as rd

n = 10
a = []
for i in range(n) :
    a.append(rd.randint(1,1000))

def selectionSort(a) :
    n = len(a)
    for i in range(n-1):
        for j in range(i+1,n):
            if a[j] < a[i] :
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
    return a

print(a)
print(selectionSort(a))