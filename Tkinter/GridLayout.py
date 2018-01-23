from tkinter import *

root = Tk()    #To create blank window with minimize, maximize and Close

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)        #Entry space in the layout
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)  #by default(column=0)  #label 1 ie. name will be on top or 1st row
label_2.grid(row=1, sticky=E)  #label 2 ie. password  will be on bottom or 2nd row
#sticky is for alignment of the text E,W,N,S ie East, West, North, South

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")  #Creates Checkbutton
c.grid(columnspan=2)    #columnspan=2 takes 2 columns


root.mainloop()     #Constantly looping ie. constantly displaying. Once we hit close button it breaks the loop
