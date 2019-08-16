#ODEV 1: Asagida ozellikleri belirtilen 4 fonksiyon belirtiniz.

#1=Tek sayi kontrolu yapan fonksiyon,
#2=Cift sayi kontrolu yapan fonksiyon,
#3=3’e bolunme kontrolu yapan fonksiyon,
#4=5’e bolunme kontrolu yapan fonksiyon.
#Bunlardan ayri 5. bir fonksiyon yazin ve bu ilksayi ve sonsayi seklinde iki parametre alsin.

#Yukarida olusturdugunuz ilk 4 fonksiyonu son olusturdugunuz fonksiyonun icinde calistirarak islemler yapiniz.
#Fonksiyon verdiginiz baslangic ve bitis sayilarina gore bir liste olusturmali ve listenin icindeki sayilari
#yukarida olusturdugunuz 4 fonksiyon yardimi ile tek - cift - 3'un kati - 5'in kati durumlarina gore kontrol etmeli.
#Uygun durumlarda ilgili fonksiyonun ciktisini vermeli.

#Orn: def sayikontrol(ilksayi,sonsayi)

#sayikontrol(1,10)
#Ornek cikti:
#1 tek sayidir
#2 cift sayidir
#3 tek sayidir
#3 ucun katidir
#4 cift sayidir
#5 tek sayidir
#5 besin katidir
#6 cift sayidir
#6 ucun katidir
#7 tek sayidir
#8 cift sayidir
#9 tek sayidir
#9 ucun katidir


print("işlem yapmak için 1'e basınız\nçıkmak için 2'basınız:")

def sayi_kontrol(ilksayi,sonsayi):
    liste=list(range(ilksayi,sonsayi))
    print(liste)
    for sayi in liste:
        cift_sayi(sayi)
        ucun_katı(sayi)
        besin_katı(sayi)

def cift_sayi(sayi):

    if sayi%2==0:
        print(sayi,"çiftsayıdır..")

    else:
        print(sayi,"teksayıdır")

def ucun_katı(sayi):

    if sayi %3==0:
        print(sayi,"üçün katıdır..")

def besin_katı(sayi):

    if sayi%5==0:
        print(sayi,"beşin katıdır..")


while True:
    secim=input("seçiminiz:")
    if secim=="1":

        ilksayi=int(input("ilk sayıyı giriniz:"))
        sonsayi=int(input("son sayıyı giriniz:"))
        print(sayi_kontrol(ilksayi,sonsayi))
        continue  # 

    if secim=="2":
        çıkış=input("çıkmak için q'ya bas:")
        if çıkış=="q":
            print("çıkılıyor...")
            break

    else:
        print("yanlış seçim...")
        
    

sayi_kontrol(ilksayi,sonsayi)




























  









