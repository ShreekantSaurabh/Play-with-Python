from tkinter import *

root = Tk()    #To create blank window with minimize, maximize and Close

"""
def printName():
    print "Hello my name is Saurabh"

button_1 = Button(root, text="Print my name", command=printName) #function binding using command arguement
"""
#The above operation can be implemented as below
def printName(event):
    print "Hello my name is Saurabh"

button_1 = Button(root, text="Print my name")
button_1.bind("<Button-1>", printName)  #<Button-1> is for left-clicking the mouse on button_1



button_1.pack()
root.mainloop()     #Constantly looping ie. constantly displaying. Once we hit close button it breaks the loop
