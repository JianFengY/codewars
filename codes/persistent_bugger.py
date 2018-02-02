# -*- coding: utf-8 -*-
'''
Created on 2018年2月2日

@author: Jeff Yang
'''

'''
Write a function, persistence, that takes in a positive parameter num and returns its 
multiplicative persistence, which is the number of times you must multiply the digits 
in num until you reach a single digit.
For example:
persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4 and 4 has only one digit.
persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2.
persistence(4) => 0   # Because 4 is already a one-digit number.
'''

from functools import reduce
from operator import mul


def persistence(n):
    """return times that multiply the digits to a single digit"""
    times = 1
    if n < 10:
        return 0
    times += persistence(reduce(lambda a, b:a * b, map(int, str(n))))
    return times
    
#     return 0 if n < 10 else persistence(reduce(mul, [int(i) for i in str(n)], 1)) + 1


print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))
