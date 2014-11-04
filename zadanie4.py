# -*- coding: utf-8 -*-

#Funkcja napisana po zajeciach
def duplikaty(lista):
    dl=len(lista)
    wynik=[]
    for i in xrange(0,dl):
        if wynik.count(lista[i])==0:
                wynik.append(lista[i])
    return sorted(wynik)

#Optymalizacja kodu:
def duplikaty2(lista):
    return list(set(lista))

lista=["kot","pies","chomik","kot","pies","pies","wydra","okon"]
print "Lista wyjsciowa: " + str(lista)
print "Wynik pierwszej funkcji: " + str(duplikaty(lista))
print "Wynik zoptymalizowanej funkcji: " + str(duplikaty2(lista))