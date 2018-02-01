# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:54:49 2017

@author: Saurabh
"""

lst1 = [1,2,3,4,5]
lst2 = [1,2,3]

lst3 = []
for i in lst1 :
    for j in lst2:
        k = (i*j)
        #print (k)
        lst3.append(k)
#print (lst3)
print (set(lst3))


lst4  = []
lst5 = []
for i in lst3:
    if (i%2 == 0):
        #print (i)
        lst4.append(i)
    
    else:
        lst5.append(i)
    
print(lst4)
print(lst5)
        
    
