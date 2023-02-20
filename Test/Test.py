# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:18:26 2022

@author: CatLoaf
"""
f = open("s63310236.csv" , 'r' , encoding="utf-8")
l = f.read()

# print(type(1))
line = ''.join(c for c in l if c not in '[]')
# print(line)
listx = line.split(',')
# print(listx)
list1 = []
while len(listx) > 2 :
    listY = [int(listx.pop(0)),int(listx.pop(0)),int(listx.pop(0))]
    list1.append(listY)



"""
amount : List
index 0,1,2 for small size with throw away,repair,good quality
index 3,4,5 for medium size with throw away,repair,good quality
index 6,7,8 for large size with throw away,repair,good quality
"""
amount = [0,0,0,0,0,0,0,0,0]
for a in list1 :
    sized = 0.5 * 3.14 * int(a.pop(0)) * int(a.pop(0))
    if sized <= 24 :
        if a[0]== 0 :
            amount[0] += 1
        elif a[0] == 1 :
            amount[1] += 1
        else :
            amount[2] += 1
    elif sized <= 92 :
        if a[0] == 0 :
            amount[3] += 1
        elif a[0] == 1 :
            amount[4] += 1
        else :
            amount[5] += 1
    else :
        if a[0] == 0 :
            amount[6] += 1
        elif a[0] == 1 :
            amount[7] += 1
        else :
            amount[8] += 1

income = 0
for i in range(len(amount)) :
    if i == 1 :
        income += amount[i] * 25
    elif i == 2 :
        income += amount[i] * 35
    elif i == 4 :
        income += amount[i] * 40
    elif i == 5 :
        income += amount[i] * 84
    elif i == 7 :
        income += amount[i] * 94
    elif i == 8 :
        income += amount[i] * 191

print("        Throw away | Repair | good")
print("Small  :   %d      %d     %d" % (amount[0] ,amount[1] ,amount[2]))
print("Medium :   %d      %d     %d" % (amount[3] ,amount[4] ,amount[5]))
print("Large  :   %d      %d     %d" % (amount[6] ,amount[7] ,amount[8]))
print("=====================================")
print("income : %d THB" % income)