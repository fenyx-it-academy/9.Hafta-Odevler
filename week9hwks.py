#ODEV 1: Asagida ozellikleri belirtilen 4 fonksiyon belirtiniz.

#Tek sayi kontrolu yapan fonksiyon,
#Cift sayi kontrolu yapan fonksiyon,
#3’e bolunme kontrolu yapan fonksiyon,
#5’e bolunme kontrolu yapan fonksiyon.
#Bunlardan ayri 5. bir fonksiyon yazin ve bu ilksayi ve sonsayi seklinde iki parametre alsin.

#Yukarida olusturdugunuz ilk 4 fonksiyonu son olusturdugunuz fonksiyonun icinde calistirarak islemler yapiniz. Fonksiyon verdiginiz baslangic ve bitis
#sayilarina gore bir liste olusturmali ve listenin icindeki sayilari yukarida olusturdugunuz 4 fonksiyon yardimi ile tek - cift - 3'un kati - 5'in kati durumlarin
#a gore kontrol etmeli. Uygun durumlarda ilgili fonksiyonun ciktisini vermeli.

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
print("""There is a function blah blah, enter the first and the second number
        you want to evaluate their range in. """)
a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))

def odd(x):
    if x % 2 != 0:
        print(x, "is an odd number.")
        yield x
    else:
        pass
    
def even(x):
    if x % 2 == 0:
        print(x, "is an even number.")
        yield x
    else:
        pass

def multipleof3(x):
    if x % 3 == 0:
        print(x, "is a multiple of 3.")
        yield x
    else:
        pass
    
def multipleof5(x):
    if x % 5 == 0:
        print(x, "is a multiple of 5.")
        yield x
    else:
        pass

def control(x, y):
    for i in range(x, y):
        odd(i)
        yield i
        even(i)
        yield i 
        multipleof3
        yield i
        multipleof5
        yield i
    
print(control(a, b))








#ODEV 2: Verilen bir sayi listesinin elemanlarindan
#tek olanlari ikiyle carpan ve hepsini toplayip sonucu veren
#bir fonksiyon yaziniz. Map, filter ve reduce kullaniniz.

from functools import reduce

#def oddmult2add(l):
    #return list(filter(lambda x: x*2, map(lambda x: x%2 != 0, l)))

a =[1,2,3,4,5,6,7,8,9,10]

#print(reduce(oddmult2add, a))

#print(reduce(oddmult2add(a)))

print(list(filter(lambda x: x*2 , map(lambda x: x%2 != 0, a))))





#The output is [True, True, True, True, True] so I could not sum up them with reduce.



#ODEV3: pzt = [ { isim: 'Fonksiyonlara calis', sure: 180, }, { isim: 'ornek coz', sure: 120, }, { isim: 'odev kontrol', sure: 20, }, { isim: 'bayramlasma', sure: 200, } ]

#sali = [ { isim: 'gelecek haftaya hazirlik', sure: 240, }, { isim: 'ornek cozumlerine devam et', sure: 180, }, { isim: 'kahve molasi', sure: 10, }, { isim: 'kitap oku', sure: 200, }, { isim: 'spor yap', sure: 40, } ]

#Not: Sureler dakika cinsindendir!

#Map, filter ve reduce kullanarak yukarida belirtilen iki gunluk plan neticesinde kac puan kazanilacagini hesaplayan bir program yaziniz.

#•	Map ile sureleri saat cinsine donusturun.
#•	Iki saatin altindaki tum rutinleri filter ile eleyin. 
#•	Sureleri saatte 20 puan kazandiracak sekilde saatlik bazda guncelleyin. 
#•	Kusurlu degerleri .round() ile yuvarlayin. 
#•	Son olarak reduce ile kullanicinin kac puan kazandigini hesaplayin.
#•	Degisken isimlerinin duzgun ve anlasilir olmasina ozen gosterin.


pzt = [ { 'isim': 'Fonksiyonlara calis', 'sure': 180, },
       { 'isim': 'ornek coz', 'sure': 120, },
       { 'isim': 'odev kontrol', 'sure': 20, },
       { 'isim': 'bayramlasma', 'sure': 200, } ]

sali = [ { 'isim': 'gelecek haftaya hazirlik', 'sure': 240, },
         { 'isim': 'ornek cozumlerine devam et', 'sure': 180, },
         { 'isim': 'kahve molasi', 'sure': 10, },
         { 'isim': 'kitap oku', 'sure': 200, },
         { 'isim': 'spor yap', 'sure': 40, } ]

twodays= pzt + sali

#keylerin isimleri ayni, ayni isimde keylerle sozluk seklinde devam etmemiz mantiksiz


#Bu twodays listesinden valuelari her dictten tek tek alacagiz.
a = []
for i in range(len(twodays)):
    a.append(list(twodays[i].values()))

#print(a)    

b = []
for i in range(len(a)):
    b.append(a[i][1])   #a listesinin icindeki listelerin 2.ogelerini
                        #b adinin verdigimiz liste ekle

#print(b)   #Su an tum sayilar bir listede. Buraya dek alles gut.

def uurconverter(l):
    return list(map(lambda x: x/60, l))  #Su an sureleri saat cinsine donusturduk

c = uurconverter(b)

#print(c)

def below2(l):
    return list(filter(lambda x: (x>2), l))

d=below2(c)

#print(d)   #Iki saatin altindaki tum rutinleri filter ile elendi.

def multiply20(l):
    return list(map(lambda x: x*20, l))#Sureleri saatte 20 puan kazandiracak sekilde saatlik bazda guncelleyin. 

e = multiply20(d)


from functools import reduce

print(reduce(lambda x, y: x+ y, list(map(round, e))))
#Kusurlu degerleri .round() ile yuvarlayin ve topluyoruz.

    


















    
