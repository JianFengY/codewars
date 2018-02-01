# -*- coding: utf-8 -*-
'''
Created on 2018年2月1日

@author: Jeff Yang
'''

'''
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.
Zero isn't an odd number and you don't need to move it. If you have an empty array, 
you need to return it.
Example:
sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
'''


def sort_array(source_array):
    """sort the odd numbers and keep the even numbers in places"""
    indexes = [i for i, v in enumerate(source_array) if v % 2 == 1]
    values = sorted([source_array[i] for i in indexes])
    for x in range(len(indexes)):
        source_array[indexes[x]] = values[x]
    return source_array

#     odds = sorted((x for x in source_array if x % 2 != 0), reverse=True)
#     return [x if x % 2 == 0 else odds.pop() for x in source_array]


print(sort_array([5, 11, 3, 2, 11, 8, 1, 11, 4]))
print(sort_array([5, 3, 1, 8, 0]))
print(sort_array([]))
