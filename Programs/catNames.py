catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames)+1) +
          ' or enter nothing to stop :')
    name= input()

    if name == '':
        break
    catNames = catNames + [name]
#print (catNames)

print('The cat names are')

#for name in catNames:
    #print(name)

for i in range(len(catNames)):
    print (catNames[i])


