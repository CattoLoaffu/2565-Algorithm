# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:35:48 2022

@author: Admin
"""
n = int(input("enter n : "))
sumx = 0
for i in range(n):
    for j in range(i+1,n):
        sumx = sumx + 1
        print(chr(65 + i)+ "-" + chr(65 + j) )
print("Line = ", sumx)