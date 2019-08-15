#odev 2 hafta 9#
#tek sayilari listeliyoruz# 
#iki ile carpıyoruz#
#ve son listeyi topluyoruz#

from functools import reduce

def tek(sayi):
    return sayi%2==1
def carp(x):
    return x*2
def topla(a,b):
    return a+b

say=range(1,10)

b=list(filter(tek,say))
print("tek sayılar:  ",b)
c=list(map(carp,b))
print("tek sayıların iki ile carpımı:  ",c)
print("son liste toplamı:  ",reduce(topla,c))

