from tkinter import *


def doNothing():
    print("ok ok I won't ...")


root = Tk()

# *****Creating Menu & SubMenu*****

menu = Menu(root)     #To create menu, use class Menu   #it is placed at top horizontal of any file eg. File, Edit, Search etc.
root.config(menu = menu)    #argument menu = object menu created from Menu(root)

subMenu = Menu(menu)      #To create submenu ie. dropdown list of a menu item
menu.add_cascade(label = "File", menu = subMenu)   #Name of Menu is File
subMenu.add_command(label = "Project", command = doNothing) #Name of the subMenu is Project. if we click the Project then it envokes the doNothing function
subMenu.add_command(label = "Program", command = doNothing)

subMenu.add_separator()    #to put a horizontal line between different submenu items
subMenu.add_command(label = "Exit", command = doNothing)

editMenu = Menu(menu)     #Creating 2nd menu item
menu.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Redo", command = doNothing)

# *****Creating Toolbar (below Menu)*****
toolbar = Frame(root, bg = "blue")
insertButton = Button(toolbar, text="Insert Image", command = doNothing)
insertButton.pack(side=LEFT, padx = 2, pady=2)      #padx , pady is leave pixels space around the label in x and y axis
printButton = Button(toolbar, text="Print", command = doNothing)
printButton.pack(side=LEFT, padx = 2, pady=2)

toolbar.pack(side = TOP, fill=X)

root.mainloop()