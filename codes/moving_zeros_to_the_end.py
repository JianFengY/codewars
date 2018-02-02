# -*- coding: utf-8 -*-
'''
Created on 2018年2月3日

@author: Jeff Yang
'''

'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving 
the order of the other elements.
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
'''


def move_zeros(array):
    """move zeros to the end"""
    return sorted(array, key=lambda x:(x == 0) and x is not False)
    
#     l = [i for i in array if isinstance(i, bool) or i != 0]
#     return l + [0] * (len(array) - len(l))


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]))
print(move_zeros([0, 1, None, 2, False, 1, 0]))
print(move_zeros(["a", "b"]))
print(move_zeros(["a"]))
print(move_zeros([0, False, 0]))
print(move_zeros([0]))
print(move_zeros([]))
