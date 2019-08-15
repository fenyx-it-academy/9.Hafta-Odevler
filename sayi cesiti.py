# ODEV 1: Asagida ozellikleri belirtilen 4 fonksiyon belirtiniz.
#
# Tek sayi kontrolu yapan fonksiyon,
# Cift sayi kontrolu yapan fonksiyon,
# 3’e bolunme kontrolu yapan fonksiyon,
# 5’e bolunme kontrolu yapan fonksiyon.
# Bunlardan ayri 5. bir fonksiyon yazin ve bu ilksayi ve sonsayi seklinde iki parametre alsin.
#
# Yukarida olusturdugunuz ilk 4 fonksiyonu son olusturdugunuz fonksiyonun icinde calistirarak islemler yapiniz. Fonksiyon verdiginiz baslangic ve bitis sayilarina gore bir liste olusturmali ve listenin icindeki sayilari tek - cift - 3'un kati - 5'in kati durumlarina gore kontrol etmeli. Uygun durumlarda ilgili fonksiyonu cagirip o duruma iliskin bir cikti vermeli.
#
# Orn: def sayikontrol(ilksayi,sonsayi)
#
# sayikontrol(1,10)
# Ornek cikti:
# 1 tek sayidir
# 2 cift sayidir
# 3 tek sayidir
# 3 ucun katidir
# 4 cift sayidir
# 5 tek sayidir
# 5 besin katidir
# 6 cift sayidir
# 6 ucun katidir
# 7 tek sayidir
# 8 cift sayidir
# 9 tek sayidir
# 9 ucun katidir

def tek(sayi):
    if sayi%2==1:
        print(sayi,'--> tek sayidir')

def cift(sayi):
    if sayi%2==0:
        print(sayi,'--> cift sayidir')

def uc_bol(sayi):
    if sayi%3==0:
        print(sayi,'--> 3 un katidir')
def bes_bol(sayi):
    if sayi%5==0:
        print(sayi,'--> 5 in katidir')
def kontrol(sayi1,sayi2):
    depo=sorted([sayi1,sayi2]) #sayi 1 > sayi2 degerleri icin bir onlem

    for sayac in range(depo[0],depo[1]):
        if sayac==0:
            print(sayac,'--> sifir')#sayi 0 dan baslarsa icin onlem
            continue
        tek(sayac)
        cift(sayac)
        uc_bol(sayac)
        bes_bol(sayac)


kontrol(-90,0)





