"""ODEV 1: Asagida ozellikleri belirtilen 4 fonksiyon belirtiniz.

Tek sayi kontrolu yapan fonksiyon,
Cift sayi kontrolu yapan fonksiyon,
3’e bolunme kontrolu yapan fonksiyon,
5’e bolunme kontrolu yapan fonksiyon.
Bunlardan ayri 5. bir fonksiyon yazin ve bu ilksayi ve sonsayi seklinde iki parametre alsin.

Yukarida olusturdugunuz ilk 4 fonksiyonu son olusturdugunuz fonksiyonun icinde calistirarak islemler yapiniz. Fonksiyon verdiginiz baslangic ve bitis sayilarina gore bir liste olusturmali ve listenin icindeki sayilari yukarida olusturdugunuz 4 fonksiyon yardimi ile tek - cift - 3'un kati - 5'in kati durumlarina gore kontrol etmeli. Uygun durumlarda ilgili fonksiyonun ciktisini vermeli.

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
9 ucun katidir"""


tek_sayi= lambda x:( x%2!=0 )
cift_sayi= lambda x:(x%2==0)
uce_bolunebilme=lambda x: (x%3==0)
bese_bolunebilme=lambda x: (x%5==0)

def toplu(sayi1,sayi2):
    for i in range(sayi1,sayi2):
        if tek_sayi(i)==True:
            print("{}. sayisi Tek sayidir".format(i))
        if cift_sayi(i) ==True:
            print("{}. sayisi Cif sayidir".format(i))
        if uce_bolunebilme(i) ==True:
            print("{}. sayisi ucun katidir".format(i))
        if bese_bolunebilme(i) ==True:
            print("{}. sayisi besin katidir".format(i))

toplu(1,10)




