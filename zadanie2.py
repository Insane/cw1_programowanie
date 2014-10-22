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
        print True
    else:
        print False

palindrom("Ikar lapal raki")
palindrom("Ikar") 

  