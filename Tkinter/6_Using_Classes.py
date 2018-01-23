from tkinter import *

class SaurabhsButtons:
    def __init__(self, master):
        #master = root
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side = LEFT)
        
        self.quitButton = Button(frame, text="Quit", command=frame.quit)   #if we click the quit button then it will terminate the main program
        self.quitButton.pack(side=LEFT)
    
    def printMessage(self):
        print "Wow, this actually worked !"

root = Tk()
obj = SaurabhsButtons(root)

root.mainloop()