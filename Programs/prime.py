# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 08:55:15 2017

@author: Saurabh 
"""

#lower = 2
#upper = 51

#print("Prime numbers between",lower,"and",upper,"are:")
lst_prime = []

for num in range(2,50):
    for i in range(2,num):
           if (num % i) == 0:
               print(num, 'equals', i, '*', num//i)
               break
    else:
        print(num, 'is a prime number')
