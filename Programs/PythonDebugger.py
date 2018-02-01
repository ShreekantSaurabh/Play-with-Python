# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 12:38:35 2017

@author: Saurabh
"""
import pdb

#def add(i,j):
#    return(i+j)
    
#def sub(i,j):
#    return(i-j)

pdb.set_trace()
def rev(tmp):
    """
    tmp should always be a list
    """
    tmp1 = tmp[::-1]
    return tmp1

def eve(tmp):
    lst = []
    for i in tmp:
        if i%2 == 0:
            #print(i)
            lst.append(i)
    return lst

def od(tmp):
    lst = []
    for i in tmp:
        if i%2 != 0:
            #print(i)
            lst.append(i)
   
    return lst
    
#if __name__ == "__main__":
    #rev([1,2,3,4])
    #eve([1,2,3,4])
    #od([1,2,3,4])