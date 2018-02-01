# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 11:24:22 2017

@author: Saurabh
"""

#r,r+ is read and write both,rb is read binary,rb+
#w,w+ is read and write both,wb,wb+
#a is append,a+,ab,ab+


fh = open("abc_new.txt", "r+")
#print(fh.read())
#print(fh.readline())

#for line in fh:
#    print(line)

#fh.write("I am writing\n")
#fh.write("I am writing1\n")
#fh.write("I am writing2\n")

#fh.write("\nI am appending\n")

#print(fh.readline())
#print(fh.tell())    #gives location including \r \n r is for Enter key stroke

#fh.seek(23)    #sets the location
#print(fh.readline())
#print(fh.tell())    #gives location

#with open("abc_new.txt", "r") as fh:      #Used for error in closing & opening the file
#    print (fh.read())

#fh.close()    #To close the file

#print(fh.read())
#fh.seek(14)
#fh.write("Reading and writing both")
#fh.close()


#print(next(fh))

#print(fh.name)  #to know the opened file
#print(fh.closed)   #to know the file is closed or not
#fh.close()
#print(fh.closed)


##Program to print line number and line
"""cnt = 0
for line in fh:
    cnt= cnt+1
    print (cnt,line[:-1]) """
    
  
"""   
for num,line in enumerate(fh):
    print (num,line)
"""   
#fh.close()

#print(fh.read())


#Program to remove empty line and print the even lines
for line in fh:
    if line[0] != "\n":
        if int(line[-2])%2 == 0:
            print(line)
    
    


    




