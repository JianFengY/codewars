# -*- coding: utf-8 -*-
'''
Created on 2018年2月1日

@author: Jeff Yang
'''

'''
You might know some pretty large perfect squares. But what about the NEXT one?
Complete the findNextSquare method that finds the next integral perfect square after 
the one passed as a parameter. Recall that an integral perfect square is an integer 
n such that sqrt(n) is also an integer.If the parameter is itself not a perfect 
square, than -1 should be returned. You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
'''

import math


def find_next_square(sq):
    """find the next square"""
    num = math.sqrt(sq)  # same as sq**0.5
    return int((num + 1) ** 2) if int(num) == num else -1
    
#     root = sq ** 0.5
#     if root.is_integer():
#         return int((root + 1) ** 2)
#     return -1

#     return int((math.sqrt(sq) + 1) ** 2) if math.sqrt(sq) % 1 == 0 else -1

    
print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(114))
