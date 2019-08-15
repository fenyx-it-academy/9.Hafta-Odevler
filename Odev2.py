# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 17:19:49 2019

@author: HP
"""

#ODEV 2: Verilen bir sayi listesinin elemanlarindan tek olanlari ikiyle carpan ve 
#        hepsini toplayip sonucu veren bir fonksiyon yaziniz. Map, filter ve reduce kullaniniz.

from functools import reduce

while True :
    cik=input("Cikmak icin q ye basiniz,sayi listesi belirlemek icin enter a basiniz ; ")
    if cik=='q':
        print('Cikiliyor...')
        break
    
    verimiz=input('Sayi giriniz:')
    yeni=list(verimiz)
    yeniliste=[int(i) for i in yeni]
    print("Listemiz ;",yeniliste)
    
    total=reduce(lambda x,y: x+y ,list(map(lambda x: 2*x, filter(lambda a: a % 2 == 1,yeniliste))))
    print(f"Sayimizdaki tek rakamlarin toplaminin iki kati {total} 'dir")

