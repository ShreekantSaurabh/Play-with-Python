while True:
    print('who are you?')
    name = input()
    if name != 'joe' :
        print('Hi ' +name +  ' you are unauthorized user')
        continue
    else:
        print('Hi joe. Type your password')
        password = input()
        if password == 'swordfish':
            break
        else :
            print('incorrect password')
print('Access granted')

