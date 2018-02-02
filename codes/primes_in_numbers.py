# -*- coding: utf-8 -*-
'''
Created on 2018年2月2日

@author: Jeff Yang
'''

'''
Given a positive number n > 1 find the prime factor decomposition of n. The result will 
be a string with the following form :
 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.
Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
'''


def prime_factors(n):
    """find the prime factor decomposition of n"""
    result = ''
    for i in range(2, n + 1):
#     for i in range(2, int(n ** 0.5)):
        count = 0
        while n % i == 0:
            n /= i
            count += 1
        if count > 0:
            result += '({}{})'.format(i, '**' + str(count) if count > 1 else '')
#             result += '({}{})'.format(i, '**%d' % count if count > 1 else '')
        if n == 1:
            return result


print(prime_factors(7775460))
print(prime_factors(86240))
