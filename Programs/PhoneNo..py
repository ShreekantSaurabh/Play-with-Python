
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4,7):
            if not text[i].isdecimal:
                return False
        if text[7] != '-' :
            return False
        for i in range(8,12):
            if not text[i].isdecimal():
                return False
        return True

#print('Enter a phone no. in xxx-xxx-xxxx Pattern')
#text = input()
#output = isPhoneNumber(text)
#if output == False:
#    print(text + ' is a not a phone number.')
#else:
#    print(text + ' is a phone number.')

print('Enter any message with phone no. (xxx-xxx-xxxx) in it')
message = input()
found = False
for i in range(len(message)):
    chunk = message[i:i+12]
    output = isPhoneNumber(chunk)
    if output == True:
        print('Phone no. is present in the message: ' + chunk)
        found = True
if found == False:
    print('Phone no. is not present in the message')
