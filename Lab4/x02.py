# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:50:04 2022

@author: Admin
"""
import random as rd
import matplotlib.pyplot as plt

point = []
px = []
py = []
conv = []

n = int(input("enter n: "))
x = list(range(1,31))
y = list(range(1,31))

for i in range(n):
    pointx = x.pop(rd.randint(0,len(x)-1))
    pointy = y.pop(rd.randint(0,len(y)-1))
    point.append([pointx,pointy])
    px.append(pointx)
    py.append(pointy)

plt.scatter(px,py,color='blue')
plt.xticks()
plt.yticks()
plt.show()


def linex(p1,p2):
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    c = p1[0]*p2[1] - p1[1]*p2[0]
    return [a , b , c]

for i in range(n):
    for j in range(i+1,n):
        ax = linex(point[i],point[j])
        countm0 = 0
        countl0 = 0
        print(ax)
        
        for k in range(n):
            if k == i or k == j:
                temp = 0
            elif ax[0]*point[k][0] + ax[1]*point[k][1] - ax[2] < 0:
                countl0 = countl0 + 1
            elif ax[0]*point[k][0] + ax[1]*point[k][1] - ax[2]  > 0:
                countm0 = countm0 + 1

        if countm0 == 0 or countl0 == 0:
            linexxx = [point[i][0],point[j][0]]
            lineyyy = [point[i][1],point[j][1]]           
            plt.plot(linexxx,lineyyy,color="red", linewidth = 3)
            if point[i] not in conv:
                conv.append(point[i])
            if point[j] not in conv:
                conv.append(point[j])         

print(conv)
plt.scatter(px,py,color='blue')            
plt.show()