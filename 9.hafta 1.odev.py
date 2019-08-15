##ODEV 1: Asagida ozellikleri belirtilen 4 fonksiyon belirtiniz.
##1.	Tek sayi kontrolu yapan fonksiyon,
##2.	Cift sayi kontrolu yapan fonksiyon,
##3.	3’e bolunme kontrolu yapan fonksiyon,
##4.	5’e bolunme kontrolu yapan fonksiyon.
##Bunlardan ayri 5. bir fonksiyon yazin ve bu ilksayi ve
##sonsayi seklinde iki parametre alsin.
##Yukarida olusturdugunuz ilk 4 fonksiyonu son olusturdugunuz
##fonksiyonun icinde calistirarak islemler yapiniz. Fonksiyon
##verdiginiz baslangic ve bitis sayilarina gore bir liste olusturmali ve
##listenin icindeki sayilari tek - cift - 3'un kati - 5'in kati durumlarina
##gore kontrol etmeli. Uygun durumlarda ilgili fonksiyonu cagirip o duruma
##iliskin bir cikti vermeli.
##Orn: def sayikontrol(ilksayi,sonsayi)
##
##sayikontrol(1,10)
##Ornek cikti:
##1 tek sayidir
##2 cift sayidir
##3 tek sayidir
##3 ucun katidir
##4 cift sayidir
##5 tek sayidir
##5 besin katidir
##6 cift sayidir
##6 ucun katidir
##7 tek sayidir
##8 cift sayidir
##9 tek sayidir
##9 ucun katidir

print("""
                SAYI KONTROL PROGRAMI
        Belirleyeceginiz araliktaki sayilari
        tek,cift,3'e bolunen ve 5'e bolunen
        diye gruplara ayirip cikti verecegiz.

                    Buyrunuz...

""")
###Fonksiyon olusturuyoruz###
###Liste yapip baslangic ve bitis sinirlarini belirliyoruz.###
###Tek,cift,3e bol, 5e bol islemlerini tanimlayip###
###For ile bu ozelliklere uyan sayilarin ciktisini aliyoruz### 
def sayikontrol(ilksayi,sonsayi):  
    liste=list(range(ilksayi,sonsayi))
    tek=list(filter(lambda x: x%2!=0,liste))
    cift=list(filter(lambda x: x%2==0,liste))
    ucebol=list(filter(lambda x: x%3==0,liste))
    besebol=list(filter(lambda x: x%5==0,liste))
    for i in liste:
        if i in tek:
            print("{} tek sayidir.".format(i))
        if i in cift:
            print("{} cift sayidir.".format(i))
        if i in ucebol:
            print("{} 3'e bolunen sayidir.".format(i))
        if i in besebol:
            print("{} 5'e bolunen sayidir.".format(i))
sayikontrol(0,0)
ilksayi=int(input("Lutfen ilk sayiyi belirleyiniz: "))
sonsayi=int(input("Simdi de ikinci sayiyi giriniz: "))
print(ilksayi,"ile",sonsayi,"arasindaki sayilarin Listesi: \n")
sonuc=sayikontrol(ilksayi,sonsayi)


























