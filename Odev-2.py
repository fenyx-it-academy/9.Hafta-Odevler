# ODEV 2: Verilen bir sayi listesinin elemanlarindan tek olanlari ikiyle carpan
# ve hepsini toplayip sonucu veren bir fonksiyon yaziniz. Map, filter ve reduce kullaniniz.

from functools import reduce

tekSayi = lambda x: x % 2 == 1
#tek sayilari True donduren fonksiyon

topla = lambda x, y: x+y
#iki sayiyi toplayan fonks.

sayilar = range(1, 10)
tekSayilar = list(filter(tekSayi, sayilar))
#sayilar listesinden tek olanlari filter ile ayirdik

print('Tek Sayilar: ', tekSayilar)
print('Toplamlari: ', reduce(topla, tekSayilar))
#reduce ile tek sayilari topladik

