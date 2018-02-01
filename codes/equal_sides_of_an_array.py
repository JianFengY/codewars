# -*- coding: utf-8 -*-
'''
Created on 2018年2月2日

@author: Jeff Yang
'''

'''
You are going to be given an array of integers. Your job is to take that array 
and find an index N where the sum of the integers to the left of N is equal to 
the sum of the integers to the right of N. If there is no index that would make 
this happen, return -1.
'''


def find_even_index(arr):
    """find the index that the sum of the left side equals to the right side"""
    for i , v in enumerate(arr):
    # for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1


print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
print(find_even_index([1, 100, 50, -51, 1, 1]))
print(find_even_index([1, 2, 3, 4, 5, 6]))
print(find_even_index([20, 10, 30, 10, 10, 15, 35]))
print(find_even_index([20, 10, -80, 10, 10, 15, 35]))
print(find_even_index([10, -80, 10, 10, 15, 35, 20]))
print(find_even_index(range(1, 100)))
print(find_even_index([0, 0, 0, 0, 0]))
print(find_even_index([-1, -2, -3, -4, -3, -2, -1]))
print(find_even_index(range(-100, -1)))
