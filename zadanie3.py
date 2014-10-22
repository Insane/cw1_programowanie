# -*- coding: utf-8 -*-

from math import sqrt

def funkcja_kwadratowa(a,b,c,x):
    return a*(x**2)+b*x+c
def miejsca_zerowe(a,b,c):
    delta=b**2-4*a*c
    x1=(-b-sqrt(delta))/(2*a)
    x2=(-b+sqrt(delta))/(2*a)
    if delta>0:
        return x1,x2
    elif delta==0:
        return -b/(2*a)
    else:
        return None
a=2
b=3
c=1
for i in xrange(-10,11):
    print "Dla parametrów a=%s, b=%s, c=%s, oraz dla:" %(a,b,c)
    print "x= %s, funkcja kwadratowa przyjmuje wartość: %s, a jej miejsca zerowe to: %s" %(i,funkcja_kwadratowa(a, b, c, i), miejsca_zerowe(a,b,c))
  