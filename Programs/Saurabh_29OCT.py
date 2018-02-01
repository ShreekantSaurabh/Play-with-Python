tmp= "This is Python Class and ToDAYS day is SUNday"
#tmp=input("Type a string\n")

def filterUpperLowercase(statement):
    """
    Counting
    Lower caseand
    Uppercase
    """
#    print (__doc__)

    tmp1 = "".join(tmp.split())
    Lcount =0
    Ucount =0

    for i in tmp1:
        if ord(i) >=65 and ord(i) <= 90:
            print (i, 'is UpperCase')
            Ucount = Ucount + 1
        else:
            print (i, 'is LowerCase')
            Lcount = Lcount + 1
    return Ucount, Lcount

print(filterUpperLowercase(tmp))
#print (__doc__)


        