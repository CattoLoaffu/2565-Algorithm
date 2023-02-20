# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 11:47:32 2022

@author: CatLoaf
"""

inx = int(input("Enter n :"))
alphabet = []

def toString(List): 
    return ''.join(List) 

def permute(a, l, r): 
    if l==r: 
        print ("A" + toString(a) +"A")
    else: 
        for i in range(l,r): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l] 
    
for i in range(inx-1) :
    x = i
    a = chr(66 + x)
    alphabet.append(a)

permute(alphabet, 0, len(alphabet)) 