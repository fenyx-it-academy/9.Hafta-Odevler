#yapilan ise karsilik kazanilan puanlar#


pazartesi=[{'isim':'Fonksiyonlara calis', 'sure': 180,},
     {'isim':'ornek coz', 'sure': 120,},
     {'isim':'odev kontrol', 'sure': 20,},
     {'isim':'pes', 'sure': 200,}]
sali=[{'isim':'voetball', 'sure': 240,},
      {'isim':'tafeltennis', 'sure': 170,},
      {'isim':'film', 'sure': 100,},
      {'isim':'dutch', 'sure': 200,},
      {'isim':'wandelen', 'sure': 40,}]
toplam=pazartesi+sali

from functools import reduce
def sayi(x):
    return x["sure"]
def uygun(x):
    if x>=120:
        return x
def yuvarla(x):
    return round(x*20/60)
def top(a,b):
    return a+b

a=list(map(sayi,toplam))
print ("sureler:  ",a)
b=list(filter(uygun,a))
print("120 dk veya fazla olan sureler:  ",b)
c=list(map(yuvarla,b))
print("puanlar:  ",c)
d=reduce(top,c)
print("toplam puaniniz tebrikler!!:  ",d)
