# -*- coding: utf-8 -*-
'''
Created on 2018年2月1日

@author: Jeff Yang
'''

'''
Implement a function that adds two numbers together and returns their sum in binary. 
The conversion can be done before, or after the addition.
The binary number returned should be a string.
'''


def add_binary(a, b):
    """add two numbers and return sum in binary"""
    return bin(a + b)[2:]
#     return '{0:b}'.format(a + b)


print(add_binary(2, 2))
print(add_binary(51, 12))
