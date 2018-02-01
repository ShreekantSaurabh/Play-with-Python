# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 11:18:02 2017

@author: Saurabh
"""

import re

#tmp = "This is Python Class \n\n"

#searchObj = re.search(r"Python", tmp)
#print(searchObj.group())

#searchObj = re.match(r"This", tmp)     #match only matches the First Word of sentence
#print(searchObj.group())

#searchObj = re.search(r"python class", tmp, re.I)     #I is for making the regex case Insensitive
#print(searchObj.group())

#searchObj = re.search(r".*", tmp, re.S)    #capital S is for \n or new line and small s for \t \r
#print(searchObj.group())

#tmp = '12345ABCDE#+?.*^$()[]{}|'


#tmp = r"This is Python Class"
#searchObj = re.search(r"Py\^thon", tmp)   #\is used for finding special character
#print(searchObj.group())

#fh = open("Regex.txt", 'r')
##print(fh.read())
#
#for line in fh:
#    searchObj = re.search(r".*\d", line)
#    print(searchObj.group())


#searchObj = re.search(r"\W{1,2}", tmp)  # {} is to define range of output length
#print(searchObj.group())

#tmp1 = '123123123456567'
#searchObj = re.search(r"(123)+?", tmp1)   #+ is greedy search but +? will print only once
#print(searchObj.group())

fh = open("email.txt", 'r')
#print(fh.read())


for email in fh:
    searchObj = re.search(r"\w{,}", email)
    print(searchObj.group())




