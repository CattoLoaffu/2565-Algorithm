# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:18:24 2022

@author: 
"""

items = [1,1,3,4,5]
knapsack = []
limit = 7

def print_solutions(current_item, knapsack, current_sum):
    #if all items have been processed print the solution and return:
    if current_item == len(items):
        print(knapsack)
        return

    #don't take the current item and go check others
    print_solutions(current_item + 1, list(knapsack), current_sum)

    #take the current item if the value doesn't exceed the limit
    if (current_sum + items[current_item] <= limit):
        knapsack.append(items[current_item])
        current_sum += items[current_item]
        #current item taken go check others
        print_solutions(current_item + 1, knapsack, current_sum )

print_solutions(0,knapsack,0)