# ODEV 1: Asagida ozellikleri belirtilen 4 fonksiyon belirtiniz.
#
# Tek sayi kontrolu yapan fonksiyon,
# Cift sayi kontrolu yapan fonksiyon,
# 3’e bolunme kontrolu yapan fonksiyon,
# 5’e bolunme kontrolu yapan fonksiyon.
# Bunlardan ayri 5. bir fonksiyon yazin ve bu ilksayi ve sonsayi seklinde iki parametre alsin.

tekSayi = lambda x: x % 2 == 1

ciftSayi = lambda x: x % 2 == 0
uceBolunen = lambda x: x % 3 == 0
beseBolunen = lambda x: x % 5 == 0

def sayiKontrol(sayi1,sayi2):
    liste = range(sayi1,sayi2)

    for i in liste:
        if tekSayi(i) == True:
            print('{} tek sayidir.'.format(i))
            if uceBolunen(i) == True:
                print('{} 3 un katidir.'.format(i))
            elif beseBolunen(i) == True:
                print('{} 5 in katidir.'.format(i))
        elif ciftSayi(i) == True:
            print('{} cift sayidir.'.format(i))
            if uceBolunen(i) == True:
                print('{} 3 un katidir.'.format(i))
            elif beseBolunen(i) == True:
                print('{} 5 in katidir.'.format(i))

sayiKontrol(1,20)