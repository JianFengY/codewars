# -*- coding: utf-8 -*-
'''
Created on 2018年2月3日

@author: Jeff Yang
'''

'''
Write function scramble(str1,str2) that returns true if a portion of str1 characters can 
be rearranged to match str2, otherwise returns false.
For example:
str1 is 'rkqodlw' and str2 is 'world' the output should return true.
str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' should return true.
str1 is 'katas' and str2 is 'steak' should return false.
Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
'''

from collections import Counter


def scramble(s1, s2):
    """show if a portion of str1 characters can be rearranged to match str2"""
#     # Inefficient algorithms. It took longer than 12000ms to complete
#     for s in s2:
#         if s in s1:
#             s1 = s1.replace(s, '', 1)
#         else:
#             return False
#     return True
    return len(Counter(s2) - Counter(s1)) == 0
    

print(scramble('wdasas', 'ddd'))
print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))
