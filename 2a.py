#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:49:40 2024

@author: liwengu
"""
#1
import datetime
x='10'
y=20
print(int(x)+y)
#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list[my_list_len - 1])
#3
my_string = 'hello world'
print(my_string.upper())
#4
z = ['a', 'b', 'c']
z.insert(3, 'd')
print(z)
#5 run all these lines at once. why does the x not display 10,followed by the 200? Fix it so it does.
x = 10
print(x)
y = 20
print(x * y)
#6
color = 'My favorite color is {}, what is yours?'.format('blue')
print(color)
#7
color = 'My favorite color is {}, what is yours?'.format('yellow')
print(color)
#8
color = f'My favorite color is {"red"}, what is yours?'
print(color)
#------------------------------------------
#9
schools = ['harris', 'booth', 'crown', 'harris', 'Harris']
schools = list(set(map(str.lower, schools)))
print("List with unique entries:", schools)
#10
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals = list(animals)
animals[animals.index('dog')] = 'cat'
animals = tuple(animals)
print("Tuple after replacing 'dog' with 'cat':", animals)
#11
my_sent = 'All that snow we had this winter sure was fun!'
my_sent = my_sent.lower().split()
print("List of words in lower case:", my_sent)



