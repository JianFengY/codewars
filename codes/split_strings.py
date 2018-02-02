# -*- coding: utf-8 -*-
'''
Created on 2018年2月2日

@author: Jeff Yang
'''

'''
Complete the solution so that it splits the string into pairs of two characters. If 
the string contains an odd number of characters then it should replace the missing 
second character of the final pair with an underscore ('_').
Examples:
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''

import re


def split_strings(s):
    """split strings into pairs of two characters"""
    s += '_' if len(s) % 2 else ''
    return [s[i:i + 2] for i in range(len(s) - 1) if not i % 2]

#     return re.findall(".{2}", s + "_")


print(split_strings("asdfadsf"))
print(split_strings("asdfads"))
print(split_strings(""))
print(split_strings("x"))
