# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:04:09 2022

@author: Admin
"""
import random as rd
matrix2x2 = []

n = int(input('enter n : '))
for i in range(n):
    rowx = ''
    for j in range(i+1,n):
        rowx = rowx + str(rd.randint(0, 1))
        
    matrix2x2.append(list(rowx.zfill(n)))
    



#print(matrix2x2)

for i in range(len(matrix2x2)):
    for j in range(0,i):
        matrix2x2[i][j] = matrix2x2[j][i]
        
        
for i in range(len(matrix2x2)):
    print(matrix2x2[i])
        