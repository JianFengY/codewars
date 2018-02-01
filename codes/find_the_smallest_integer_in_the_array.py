# -*- coding: utf-8 -*-
'''
Created on 2018年2月1日

@author: Jeff Yang
'''

'''
Given an array of integers your solution should find the smallest integer.
For example:
Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
'''

import sys


def find_smallest_int(arr):
    """find the smallest integer"""
    return min(arr)


print(find_smallest_int([78, 56, 232, 12, 11, 43]))
print(find_smallest_int([78, 56, -2, 12, 8, -33]))
print(find_smallest_int([0, -1 - sys.maxsize, sys.maxsize]))
