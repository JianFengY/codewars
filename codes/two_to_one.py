# -*- coding: utf-8 -*-
'''
Created on 2018年2月1日

@author: Jeff Yang
'''

'''
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, 
the longest possible, containing distinct letters,each taken only once - coming from s1 
or s2.
Examples: a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"
a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''


def longest(s1, s2):
    """sort and distinct letters"""
    s = sorted(set(s1 + s2))
    return ''.join(s)


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))
