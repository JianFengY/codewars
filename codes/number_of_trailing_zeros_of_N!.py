# -*- coding: utf-8 -*-
'''
Created on 2018年2月3日

@author: Jeff Yang
'''

'''
Write a program that will calculate the number of trailing zeros in a factorial 
of a given number.N! = 1 * 2 * 3 * ... * N
Be careful 1000! has 2568 digits...
Examples:
zeros(6) = 1  # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
zeros(12) = 2  # 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the 
number of zeros.
'''
from functools import reduce
import math


def zeros(n):
    """calculate number of trailing zeros"""

#     other ways to calculate factorial
#     result = reduce(lambda x, y:x * y, range(1, n + 1))
#     def fact(n):
#         return +(n <= 1) or n * fact(n - 1)

#     # Inefficient algorithms. It took longer than 12000ms to complete
#     result = math.factorial(n)
#     return [i for i in range(len(str(result)[::-1])) if int(str(result)[::-1][i]) != 0][0]
    result = 0
    while n >= 5:
        n //= 5
        result += n
    return result

#     return n // 5 + zeros(n // 5) if n // 5 else 0

        
print(zeros(6))
print(zeros(12))
print(zeros(21))
