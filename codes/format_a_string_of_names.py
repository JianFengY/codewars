# -*- coding: utf-8 -*-
'''
Created on 2018年2月2日

@author: Jeff Yang
'''

'''
Given: an array containing hashes of names
Return: a string formatted as a list of names separated by commas except for the 
last two names, which should be separated by an ampersand.
Example:
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])  #'Bart, Lisa & Maggie'
namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])  # 'Bart & Lisa'
namelist([ {'name': 'Bart'} ])  # 'Bart'
namelist([])  # ''
'''


def namelist(names):
    """format names with commas and ampersand"""
    return '' if len(names) == 0 else ', '.join([x['name'] for x in names[:-1]]) + \
        ' & ' + names[-1]['name'] if len(names) > 1 else names[0]['name']

#     return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ", 1)[::-1]
    
#     if len(names) > 1:
#         return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), names[-1]['name'])
#     elif names:
#         return names[0]['name']
#     else:
#         return ''


print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(namelist([{'name': 'Bart'}]))
print(namelist([]))
