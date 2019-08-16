##ODEV 1:
##Asagida ozellikleri belirtilen 4 fonksiyon belirtiniz.
##1. Tek sayi kontrolu yapan fonksiyon,
##2. Cift sayi kontrolu yapan fonksiyon,
##3. 3’e bolunme kontrolu yapan fonksiyon,
##4. 5’e bolunme kontrolu yapan fonksiyon.
##
##Bunlardan ayri 5. bir fonksiyon yazin ve bu ilksayi ve sonsayi seklinde iki parametre alsin.
##
##Yukarida olusturdugunuz ilk 4 fonksiyonu son olusturdugunuz fonksiyonun icinde calistirarak islemler yapiniz.
##Fonksiyon verdiginiz baslangic ve bitis sayilarina gore bir liste olusturmali ve listenin icindeki sayilari
##tek - cift - 3'un kati - 5'in kati durumlarina gore kontrol etmeli. Uygun durumlarda ilgili fonksiyonu cagirip o 
##duruma iliskin bir cikti vermeli. 
##Orn: def sayikontrol(ilksayi,sonsayi)
##
##	sayikontrol(1,10)
##	Ornek cikti:
##	1 tek sayidir
##	2 cift sayidir
##	3 tek sayidir
##	3 ucun katidir
##	4 cift sayidir
##	5 tek sayidir
##	5 besin katidir
##	6 cift sayidir
##	6 ucun katidir
##	7 tek sayidir
##	8 cift sayidir
##	9 tek sayidir
##	9 ucun katidir

##1.Odev:Tek sayi kontrolu yapan fonksiyon,

def TekSayi(tek):
    if tek % 2 != 0:
        print(tek,"Tek sayidir")
        return tek
    else:
        print(tek,"Teksayi degil")
TekSayi(11)

##2. Cift sayi kontrolu yapan fonksiyon,
def CiftSayi (cift):
    if cift % 2 == 0:
        print(cift,"Cift sayidir")
        return cift
    else:
        print(cift,"Ciftsayi degil")
CiftSayi(11)

##3. 3’e bolunme kontrolu yapan fonksiyon,
def UceBolunme(uc):
    if uc % 3 == 0:
        print(uc,"Uce bolunebilir")
        return uc
    else:
        print(uc,"Uce bolunemez")
UceBolunme(11)

##4. 5’e bolunme kontrolu yapan fonksiyon.
def BeseBolunme(bes):
    if bes % 5 == 0:
        print(bes,"Bese bolunebilir")
        return bes
    else:
        print(bes,"Bese bolunemez")
BeseBolunme(11)

##5. bir fonksiyon yazin ve bu ilksayi ve sonsayi seklinde iki parametre alsin.
##5. Fonksiyon sadece listeyi olusturup ilk 4 fonksiyonu cagirmali.
##Bolunebilme kontrollerini kendi yapmamali.

def IlkSon(ilk,son):
    global liste
    liste=[]
    for i in range(1,10):
        if i not in liste:
            liste+=[int(i)]
    return liste
IlkSon(1,10)

for i in liste:
    TekSayi(liste[int(i)-1])
    CiftSayi(liste[int(i)-1])
    UceBolunme(liste[int(i)-1])
    BeseBolunme(liste[int(i)-1])













