# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 18:15:30 2017

@author: Saurabh
"""
"""
stat = 'green-red-yellow-black-white'

stat_list = stat.split("-")

sorted_list = sorted(stat_list)

join_sorted_list = "-".join(sorted_list)
"""

""""
import functools
lst=['1','2','3','4','5','6']
print(functools.reduce(lambda x,y: (x[0],y), lst))
"""

import functools
a = [1,2,3,4]
#b = [17,12,11,10]
#c = [-1,-4,5,9]
#print(list(map(lambda x,y,z:x+y+z,a,b,c)))

odd_numbers = print(list(filter(lambda x: x % 2 != 0, a)))
even_numbers = print(list(filter(lambda x: x % 2 == 0, a)))