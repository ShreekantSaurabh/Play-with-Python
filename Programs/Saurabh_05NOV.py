# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 11:17:43 2017

@author: Saurabh
"""


import logging
#Order : DEBUG, INFO, WARNING, ERROR, AND CRITICAL

logging.basicConfig(filename="sample_log.txt", level = logging.DEBUG, filemode = 'w')
logging.debug("This is an debug message")
logging.info("This is an debug message")
logging.warning("This is an warning message")
logging.error("This is an error message")
logging.critical("This is an critical message")
#
#fh = open("sample_log.txt", "r+")
#fh.close()

#def div(a,b):
#    try:
#        print(a/b)
#    except ZeroDivisionError as var:
#        print("Root cause of crash is " + str(var))
#        
#div(1,0)


#def div(a,b):
#    try:
#        print(a/b)
#    except TypeError as var:
#        print("Root cause of crash is " + str(var))
#        
#div(1,"a")



#def div(a,b):
#    try:
#        print(a/b)
#    except TypeError as var:
#        print("Root cause of crash is " + str(var))
#    finally:
#        print("I am finally block")
#        
#div(1,"a")

#def div(a,b):
#    assert(a/b > 1), "Greater than 1 Division value not allowed"
#
#try:
#    div(1,2)
#except AssertionError as AE:
#    print("EX: " + str(AE))
#    
