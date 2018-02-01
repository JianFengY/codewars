# -*- coding: utf-8 -*-
'''
Created on 2018年2月1日

@author: Jeff Yang
'''

'''
The goal of this exercise is to convert a string to a new string where each character
in the new string is '(' if that character appears only once in the original string, 
or ')' if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate.
Examples:
"din" => "((("
"recede" => "()()()"
"Success" => ")())())"
"(( @" => "))(("
'''


def duplicate_encode(word):
    """convert string to '(' or ')'"""
    return ''.join(['(' if word.lower().count(i) is 1 else ')' for i in word.lower()])


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
