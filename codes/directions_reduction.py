# -*- coding: utf-8 -*-
'''
Created on 2018年2月3日

@author: Jeff Yang
'''

'''
Write a function dirReduc which will take an array of strings and returns an array of 
strings with the needless directions removed (W<->E or S<->N side by side).
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not 
reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly 
opposite of each other and can't become such. Hence the result path is itself : 
["NORTH", "WEST", "SOUTH", "EAST"].
Examples:
dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]); // => ["WEST"]
dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]); // => []
'''


def dirReduc(arr):
    """reduce directions"""
    test = [["NORTH", "SOUTH"], ["SOUTH", "NORTH"], ["EAST", "WEST"], ["WEST", "EAST"]]
    for i in range(len(arr) - 1):
        if arr[i:i + 2] in test:
            arr.pop(i)
            arr.pop(i)
#             del(arr[i:i + 2])
            return dirReduc(arr)
    return arr

#     opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
#     new_plan = []
#     for d in arr:
#         if new_plan and new_plan[-1] == opposite[d]:
#             new_plan.pop()
#         else:
#             new_plan.append(d)
#     return new_plan

    
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))
