# -*- coding: utf-8 -*-
'''
Created on 2018年2月1日

@author: Jeff Yang
'''

'''
Given a list lst and a number N, create a new list that contains each number of lst 
at most N times without reordering. For example if N = 2, and the input is 
[1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 
1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
Example:
delete_nth ([1,1,1,1],2) # return [1,1]
delete_nth ([20,37,20,21],1) # return [20,37,21]
'''


def delete_nth(order, max_e):
    """delete occurrences of an element if it occurs more than n times"""
    return [x for i, x in enumerate(order) if order[i::-1].count(x) <= max_e]
#     return [x for i, x in enumerate(order) if order[:i + 1].count(x) <= max_e]

#     ans = []
#     for o in order:
#         if ans.count(o) < max_e: ans.append(o)
#     return ans


print(delete_nth([1, 1, 1, 1], 2))
print(delete_nth([20, 37, 20, 21], 1))
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
