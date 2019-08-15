# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 00:54:35 2019

@author: HP
"""

# 1) OdevODEV 1: Asagida ozellikleri belirtilen 4 fonksiyon belirtiniz.

#  Tek sayi kontrolu yapan fonksiyon,
#  Cift sayi kontrolu yapan fonksiyon,
#  3’e bolunme kontrolu yapan fonksiyon,
#  5’e bolunme kontrolu yapan fonksiyon.
#  Bunlardan ayri 5. bir fonksiyon yazin ve bu ilksayi ve sonsayi seklinde iki parametre alsin.

#  Yukarida olusturdugunuz ilk 4 fonksiyonu son olusturdugunuz fonksiyonun icinde calistirarak islemler yapiniz. 
#  Fonksiyon verdiginiz baslangic ve bitis sayilarina gore bir liste olusturmali ve 
#  listenin icindeki sayilari tek - cift - 3'un kati - 5'in kati durumlarina gore kontrol etmeli. 
#  Uygun durumlarda ilgili fonksiyonu cagirip o duruma iliskin bir cikti vermeli.


ilksayi=int(input("Baslangic Sayisi ="))
sonsayi=int(input("Bitis Sayisi     ="))
if ilksayi>sonsayi:
    ilksayi,sonsayi=sonsayi,ilksayi
def sayi_kontrol(ilksayi,sonsayi):
    liste = list(range(ilksayi,sonsayi))
    print("\nListe =",liste,'\n')
    Tek   =list(map(lambda x: f'{x} tek sayidir\n'  , filter(lambda a: a % 2 == 1, liste)))
    Cift  =list(map(lambda y: f'{y} cift sayidir\n' , filter(lambda b: b % 2 == 0, liste)))
    Uckat =list(map(lambda z: f'{z} ucun katidir\n' , filter(lambda c: c % 3 == 0, liste)))
    Beskat=list(map(lambda t: f'{t} besin katidir\n', filter(lambda d: d % 5 == 0, liste)))
    print(*Tek,*Cift,*Uckat,*Beskat)
sayi_kontrol(ilksayi,sonsayi)  


# %% Fonksiyonlari 5.fonksiyonda cagirarak;

tek   =lambda a: a % 2 == 1
cift  =lambda b: b % 2 == 0
uckat =lambda c: c % 3 == 0
beskat=lambda d: d % 5 == 0

ilksayi=int(input("Baslangic Sayisi ="))
sonsayi=int(input("Bitis Sayisi     ="))
if ilksayi>sonsayi:
    ilksayi,sonsayi=sonsayi,ilksayi
print('\nSonuclar...;')
def secim(ilksayi,sonsayi):
    for sayi in range(ilksayi,sonsayi):
        if tek(sayi)==True:
            print(f'{sayi} tekdir')
        if cift(sayi)==True:
            print(f'{sayi} cifttir')
        if uckat(sayi)==True:
            print(f'{sayi} ucun katidir')
        if beskat(sayi)==True:
            print(f'{sayi} besin katidir')
secim(ilksayi,sonsayi)
            

# %% Ucuncu yol fonksiyon tanimlayarak;

def ciftek(sayi):
    if sayi % 2 == 0:
        print(f'{sayi} cift sayidir...')
    else:
        print(f'{sayi} tek sayidir...')

def ucmu(sayi):
    if sayi % 3 == 0:
        print(f'{sayi} ucun katidir...')

def besmi(sayi):
    if sayi % 5 == 0:
        print(f'{sayi} besin katidir...')
        
        

ilksayi=int(input("Baslangic Sayisi ="))
sonsayi=int(input("Bitis Sayisi     ="))
if ilksayi>sonsayi:
    ilksayi,sonsayi=sonsayi,ilksayi

def sayi_kontrol(ilksayi,sonsayi):
    liste = list(range(ilksayi,sonsayi))
    print("\nListe =",liste,'\n')
    for sayi in liste:
        ciftek(sayi)
        ucmu(sayi)
        besmi(sayi)
    
sayi_kontrol(ilksayi,sonsayi)  















