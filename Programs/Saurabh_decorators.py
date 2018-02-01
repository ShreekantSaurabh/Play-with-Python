# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 15:49:48 2017

@author: Saurabh
"""


import time

def decoration(func):
    def inner():
        start_time = time.time()
        print(start_time)
        func(value)
        end_time = time.time()
        print(end_time)
        
    return inner


@decoration
def even_odd(number):
    if number % 2 == 0:
        print(str(number) + ' is even')
    else:
        print(str(number) + ' is odd')

even_odd(120)