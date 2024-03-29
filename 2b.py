#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:00:15 2024

@author: liwengu
"""
#1
i = 0
while i < 10:
    if i < 5:
        print('little')
    elif i == 5:
        pass
    else:
        print('big')
    print('Finished!')
    i += 1

#2
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
#3
start_list = [[2, 3, 4], [6, 8, 9]]
result = []
for sublist in start_list:
    for num in sublist:
        result.append(num - 1)
result = [num - 1 for sublist in start_list for num in sublist]
print(result)
#4
import datetime
start_dict = {'noah': '2/23/1999', 'sarah': '9/1/2001', 'zach': '8/8/2005'}
converted_dict = {}
for name, date_str in start_dict.items():
    date_obj = datetime.datetime.strptime(date_str, '%m/%d/%Y')
    converted_dict[name.capitalize()] = date_obj
converted_dict = {name.capitalize(): datetime.datetime.strptime(date_str, '%m/%d/%Y') for name, date_str in start_dict.items()}
print(converted_dict)

