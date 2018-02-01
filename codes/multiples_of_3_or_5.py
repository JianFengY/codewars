# -*- coding: utf-8 -*-
'''
Created on 2018年2月1日

@author: Jeff Yang
'''

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 
3 or 5 below the number passed in.
Note: If the number is a multiple of both 3 and 5, only count it once.
'''


def get_sum_of_multiples(number):
    """calculate the sum of numbers that are multiples of 3 or 5"""
    return sum(num for num in range(number) if num % 3 == 0 or num % 5 == 0)


print(get_sum_of_multiples(10))
