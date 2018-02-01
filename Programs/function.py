# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 11:23:23 2017

@author: Saurabh
"""


def data(name, age,*args,**kwargs):
    print (name)
    print (age)
    print (args)
    print (kwargs)
    

data('learn',10,12,13,kw1='XYZ', kw2=19)


#lambda var:expr,
"""
lst9 = [1,2,3,4,5]
str1 =5
multi=lambda  : lst9[x]**2, lst9[x]
print (multi)
"""
"""import functools
lst = [1,2,3,4,5,6]
#tmp = lambda x:x%2, lst
#print(tmp(lst))
#print(tmp)
#print (filter (lambda x:x%2, lst))

print (functools.reduce(lambda x,y:x*y,lst))"""







