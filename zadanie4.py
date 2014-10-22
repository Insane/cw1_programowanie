def duplikaty(lista):
    dl=len(lista)
    wynik=[]
    for i in xrange(0,dl):
        if wynik.count(lista[i])==0:
                wynik.append(lista[i])
    print wynik    

duplikaty(["kot","pies","chomik","kot","pies","pies","wydra","okon"])