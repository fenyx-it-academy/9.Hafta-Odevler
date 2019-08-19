#ODEV 1: Asagida ozellikleri belirtilen 4 fonksiyon belirtiniz.
#
#Tek sayi kontrolu yapan fonksiyon,
#Cift sayi kontrolu yapan fonksiyon,
#3’e bolunme kontrolu yapan fonksiyon,
#5’e bolunme kontrolu yapan fonksiyon.
#Bunlardan ayri 5. bir fonksiyon yazin ve bu ilksayi ve sonsayi seklinde iki
#parametre alsin.

#Yukarida olusturdugunuz ilk 4 fonksiyonu son olusturdugunuz fonksiyonun icinde
#calistirarak islemler yapiniz. Fonksiyon verdiginiz baslangic ve bitis
#sayilarina gore bir liste olusturmali ve listenin icindeki sayilari yukarida
#olusturdugunuz 4 fonksiyon yardimi ile tek - cift - 3'un kati - 5'in kati
#durumlarina gore kontrol etmeli. Uygun durumlarda ilgili fonksiyonun ciktisini
#vermeli.

teksayi = lambda sayi: sayi%2==1
ciftsayi = lambda sayi: sayi%2==0
uckat = lambda sayi: sayi%3==0
beskat = lambda sayi: sayi%5==0
# lambda ile 4 farkli istenen fonksiyonlar olusturuldu.

def kontrol(sayi):
    if teksayi(sayi):
        print(sayi,">>> bir tek sayidir.")
    if ciftsayi(sayi):
        print(sayi,">>> bir cift sayidir.")
    if uckat(sayi):
        print(sayi,">>> ucun bir katidir.")
    if beskat(sayi):
        print(sayi,">>> besin bir katidir.")
# kontrol fonksiyonu ile gelen her deger 4 fonksiyonda calistirilip hangisi kosulu sagliyosa deger donduruldu.
ilksayi=int(input("Lutfen ilk sayiyi giriniz:"))
sonsayi=int(input("Lutfen son sayiyi giriniz:"))
if ilksayi>sonsayi:
    ilksayi,sonsayi=sonsayi,ilksayi
# bu if bloguyla kullanicinin ilk sayiyi buyuk girmesi ile programin bitmesi engellendi.
list(map(kontrol,range(ilksayi,sonsayi)))  # map ile kontrol fonksiyonuna istenen araliktaki her deger sirasiyla gonderildi.

