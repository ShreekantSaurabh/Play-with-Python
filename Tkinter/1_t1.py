from tkinter import *

root = Tk()    #To create blank window with minimize, maximize and Close
#theLabel = Label(root, text = 'This is too easy')    #Created a label
#theLabel.pack()     #pack() is used To display on the screen

topFrame = Frame(root)  #Dividing the screen in top and bottom frame
topFrame.pack()        #By default side = TOP

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)    #side = BOTTOM puts the frame in bottom of the window

button1 = Button(topFrame, text="Button 1", fg='red') #button1 will be present in top frame with name Button1 written in red color
button2 = Button(topFrame, text="Button 2", fg='blue') #button2 will be present in top frame with name Button1 written in blue color
button3 = Button(topFrame, text="Button 3", fg='green') #button3 will be present in top frame with name Button1 written in green color
button4 = Button(bottomFrame, text="Button 4", fg='purple') #button4 will be present in top frame with name Button1 written in purple color

button1.pack(side=LEFT)   #pack() is used To display on the screen
button2.pack(side=LEFT)   #By default pack() display in vertical order
button3.pack(side=LEFT)   #side=LEFT packs the button in horizontal order
button4.pack(side=BOTTOM)

root.mainloop()     #Constantly looping ie. constantly displaying. Once we hit close button it breaks the loop



