# -*- coding: utf-8 -*-
'''
Created on 2018年2月1日

@author: Jeff Yang
'''

'''
In this kata you are required to, given a string, replace every letter with 
its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
a being 1, b being 2, etc.
As an example:
alphabet_position("The sunset sets at twelve o' clock.")
return"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11".
'''


def alphabet_position(text):
    """replace letter with its position in the alphbet"""
    return ' '.join([str(ord(c.upper()) - 64) for c in text if c.isalpha()])


print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))
