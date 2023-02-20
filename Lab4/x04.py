# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 11:56:45 2022

@author: CatLoaf
"""
import random as rd


a = int(input("enter n : "))
lim = int(input("enter weight : "))
weight = []
price = []

possWay = []
for i in range(a) :
    weight.append(rd.randint(1, 5))
    price.append(rd.randint(1, 50))
    
for i in range(a):
    print("item %d : weight %d price %d" % (i+1,weight[i],price[i]))
    
    
def print_solutions(current_item, possWay, current_sum , current_price): 
    if current_item == len(weight):
        print("total price %d with item %s" % (current_price , possWay))
        return

    print_solutions(current_item + 1, list(possWay), current_sum , current_price)

    if (current_sum + weight[current_item] <= lim):
        possWay.append(current_item+1)
        current_sum += weight[current_item]
        current_price += price[current_item]
        print_solutions(current_item + 1, possWay, current_sum ,current_price )

print("Possible way is :")
print_solutions(0,possWay,0,0)