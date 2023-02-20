# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:10:02 2022

@author: CatLoaf
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

visited = []
queue = []

def bfs(visited, graph, node): 
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0) 
        print (m, end = " ") 

    for neighbour in graph[m]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)

g = {}
for i in range(n) :
    g[i] = set(matrix2x2[i])
print(g)
bfs(visited, g, 0)