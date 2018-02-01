#! python3

import re, pyperclip

# Todo : Create a regex for phone numbers

re.compile(r'''

((\d\d\d)|(\(\d\d\d\)))?
(\s|-)
\d\d\d\d
(((ext(\.)?\s)|x)
(\d{2,5}))?

''', re.VERBOSE)


# Todo : Create a regex for email adress

emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+

''', re.VERBOSE)

# Todo : Get the text off the clipboard

text ==pyperclip.paste()


# Todo : Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#Todo : Copy the extraced email/Phone to the clipboard
results = '\n'.join(allPhonenumbers)+ '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
