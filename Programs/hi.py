# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 08:55:15 2017

@author: Saurabh 
"""


lst_prime = []

num= 2
count = 0
while True :
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        print(str(num) + " is prime")
        lst_prime.append(str(num))
        count=count+1
    num=num+1
    if count == 50:
        break
print(lst_prime)    
        