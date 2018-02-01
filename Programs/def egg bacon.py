def spam():
    eggs = 99
    bacon()
    print('spam local ' + str(eggs))

def bacon():
    eggs = 0
    print('bacon local ' + str(eggs))

spam()
bacon()

eggs = 'global'
print(eggs)
