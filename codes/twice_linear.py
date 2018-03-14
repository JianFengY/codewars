# -*- coding: utf-8 -*-
'''
Created on 2018年3月14日

@author: Jeff Yang
'''

'''
Consider a sequence u where u is defined as follows:
The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
# Task: Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u.
# Example: dbl_linear(10) should return 22
# Note: Focus attention on efficiency
'''


def dbl_linear(n):
    u = [1]
    x_index, y_index = 0, 0
    while len(u) <= n:
        x = 2 * u[x_index] + 1
        y = 3 * u[y_index] + 1
        if x < y:
            if x != u[-1]:
                u.append(x)
            x_index += 1
        else:
            if y != u[-1]:
                u.append(y)
            y_index += 1
    return u[n]
    
#     u = [1]
#     i = 0
#     j = 0
#     while len(u) <= n:
#         x = 2 * u[i] + 1
#         y = 3 * u[j] + 1
#         if x <= y:
#             i += 1
#         if x >= y:
#             j += 1
#         u.append(min(x,y))
#     return u[n]

#     num_list = [1]
#     for i in num_list:
#         num_list.append((i * 2) + 1)
#         num_list.append((i * 3) + 1)
#     if len(num_list) > n * 10:
#         break
#     return sorted(list(set(num_list)))[n]


print(dbl_linear(20))
