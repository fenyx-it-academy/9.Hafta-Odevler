print('b.')
'''
ODEV 1: Asagida ozellikleri belirtilen 4 fonksiyon belirtiniz.

Tek sayi kontrolu yapan fonksiyon,
Cift sayi kontrolu yapan fonksiyon,
3’e bolunme kontrolu yapan fonksiyon,
5’e bolunme kontrolu yapan fonksiyon.
Bunlardan ayri 5. bir fonksiyon yazin ve bu ilksayi ve sonsayi seklinde iki parametre alsin.

Yukarida olusturdugunuz ilk 4 fonksiyonu son olusturdugunuz fonksiyonun icinde calistirarak islemler yapiniz. 
Fonksiyon verdiginiz baslangic ve bitis sayilarina gore bir liste olusturmali ve 
listenin icindeki sayilari tek - cift - 3'un kati - 5'in kati durumlarina gore kontrol etmeli. 
Uygun durumlarda ilgili fonksiyonu cagirip o duruma iliskin bir cikti vermeli.

Orn: def sayikontrol(ilksayi,sonsayi)

sayikontrol(1,10)
Ornek cikti:
1 tek sayidir
2 cift sayidir
3 tek sayidir
3 ucun katidir
4 cift sayidir
5 tek sayidir
5 besin katidir
6 cift sayidir
6 ucun katidir
7 tek sayidir
8 cift sayidir
9 tek sayidir
9 ucun katidir
'''

def sayi_kontrol(baslangic,bitis):
    def tek(i):         # tek sayi oldugunu kontrol eden fonksiyon
        if i % 2 == 1:
            return i
    def cift(i):        # cift sayi oldugunu kontrol eden fonksiyon
        if i % 2 == 0:
            return i
    def ucunkati(i):    # 3 un kati ve tek sayi oldugunu kontrol eden fonksiyon
        if i % 3 == 0:
            return i
        elif i % 2 == 1 and i % 3 == 0:
            return i
    def besinkati(i):   # 5 in kati ve tek sayi oldugunu kontrol eden fonksiyon
        if i % 5 == 0:
            return i
        elif i % 2 == 1 and i % 5 == 0:
            return i
    for i in range(baslangic,bitis):    # for range ile baslangictan bitise kadar olan araligindaki sayilara bakti
        if tek(i) :                     # if ile fonksiyonlarimizi cagirdik... uygun ciktilari aldik
            print(f'{i} tek sayidir')
        if cift(i):
            print(f'{i} cift sayidir')
        if ucunkati(i):
            print(f'{i} ucun katidir')
        if besinkati(i):
            print( f'{i} besin katidir')
# baslangic ve bitis sayilarimizi input aldik
baslangic=int(input('baslangic sayisini giriniz...:'))
bitis=int(input('bitis sayisini giriniz.......:'))

sayi_kontrol(baslangic,bitis)   # sayi kontrol fonk cagirdik.
