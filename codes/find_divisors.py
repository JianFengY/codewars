# -*- coding: utf-8 -*-
'''
Created on 2018年2月1日

@author: Jeff Yang
'''

'''
Create a function named divisors/Divisors that takes an integer and returns an array
with all of the integer's divisors(except for 1 and the number itself). 
If the number is prime return the string '(integer) is prime' 
'''


def divisors(integer):
    """find number's divisors"""
    results = [x for x in range(2, int(integer / 2) + 1) if (integer % x == 0)]
    return results if len(results) > 0 else str(integer) + ' is prime'
#     return [n for n in range(2, integer) if not integer % n] or '{} is prime'.format(integer)
    

print(divisors(15))
print(divisors(12))
print(divisors(13))
