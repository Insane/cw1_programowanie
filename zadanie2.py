#Funkcja napisana po zajeciach:
def palindrom(arg1):
    l1=0
    arg2=str(arg1).lower()
    argument=str(arg2).replace(" ", "")
    dl=len(argument)
    l2=dl
    for i in xrange(0,dl):
       if argument[i]==argument[dl-1]:
            dl=dl-1
            l1=l1+1
    if l1==l2:
        return True
    else:
        return False

#Zoptymalizowana funkcja:
def palindrom2(arg1):
    arg1=(str(arg1).replace(" ", "")).lower()
    if arg1==arg1[::-1]:
        return True
    else:
        return False
    
print palindrom("Ikar lapal raki")
print palindrom("Ikar") 
print palindrom2("Ikar lapal raki")
print palindrom2("Ikar") 