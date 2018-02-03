# -*- coding: utf-8 -*-
'''
Created on 2018年2月3日

@author: Jeff Yang
'''

'''
Make a function that will return a greeting statement that uses an input; your program 
should return, "Hello, <name> how are you doing today?".
[Make sure you type the exact thing I wrote or the program may not execute properly]
'''


def greet(name):
    """greet"""
    return 'Hello, {} how are you doing today?'.format(name)

#     return "Hello, %s how are you doing today?" % name


print(greet('Ryan'))
