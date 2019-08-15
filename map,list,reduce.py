#odev 2 hafta 9#
#tek ssayýlarý listeliyoruz 
iki ile carpýyoruz
ve son listeyi topluyoruz#

from functools import reduce

def tek(sayi):
    return sayi%2==1
def carp(x):
    return x*2
def topla(a,b):
    return a+b

say=range(1,10)

b=list(filter(tek,say))
print("tek sayýlar:  ",b)
c=list(map(carp,b))
print("tek sayýlarýn iki ile carpýmý:  ",c)
print("son liste toplamý:  ",reduce(topla,c))

