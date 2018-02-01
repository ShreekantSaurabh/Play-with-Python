birthdays = {'Alice':'Apr 1', 'Bob':'May 1', 'Carol':'June 1'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday info. for' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print ('Birthday database updated.')

        
print(birthdays)
