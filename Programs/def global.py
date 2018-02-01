eggs = 'global'

def spam():
    print(eggs)  #output : global
    global eggs
    eggs = 'spam'
    print(eggs)   #output : spam

def bacon():
    #print(eggs) gives error. Since variable egg cant be used before it is defined locally.
    eggs = 'bacon'
    print(eggs)


def ham():
    print(eggs)
    global eggs
    eggs = 'ham'
    print(eggs)
    

spam()
print(eggs)       #output : spam , since spam value is assigned to eggs variable.
bacon()
ham()

