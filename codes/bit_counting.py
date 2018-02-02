# -*- coding: utf-8 -*-
'''
Created on 2018年2月2日

@author: Jeff Yang
'''

'''
Write a function that takes an (unsigned) integer as input, and returns the number 
of bits that are equal to one in the binary representation of that number.
Example: The binary representation of 1234 is 10011010010, so the function should 
return 5 in this case
'''


def count_bits(n):
    """count number of bits that are equal to 1"""
    return bin(n).count('1')

#     return '{:b}'.format(n).count('1')


print(count_bits(0))
print(count_bits(4))
print(count_bits(7))
print(count_bits(9))
print(count_bits(10))
