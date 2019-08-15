# ODEV 1: Asagida ozellikleri belirtilen 4 fonksiyon belirtiniz.
#
# Tek sayi kontrolu yapan fonksiyon,
# Cift sayi kontrolu yapan fonksiyon,
# 3’e bolunme kontrolu yapan fonksiyon,
# 5’e bolunme kontrolu yapan fonksiyon.
# Bunlardan ayri 5. bir fonksiyon yazin ve bu ilksayi ve sonsayi seklinde iki parametre alsin.

tekSayi = lambda x: x % 2 == 1
#teksayilari True donduren fonks.
ciftSayi = lambda x: x % 2 == 0
#ciftsayilari True donduren fonks.
uceBolunen = lambda x: x % 3 == 0
#3e tam bolunenleri True donduren fonks.
beseBolunen = lambda x: x % 5 == 0
#5e tam bolunenleri True donduren fonks.

def sayiKontrol(sayi1,sayi2):
    liste = range(sayi1,sayi2)

    for i in liste:
        if tekSayi(i) == True:
            #listeden secilen eleman teksayi ise
            print('{} tek sayidir.'.format(i))
            if uceBolunen(i) == True:
                # listeden secilen eleman 3e tam bolunuyor ise
                print('{} 3 un katidir.'.format(i))
            elif beseBolunen(i) == True:
                # listeden secilen eleman 5e tam bolunuyor ise
                print('{} 5 in katidir.'.format(i))
        elif ciftSayi(i) == True:
            # listeden secilen eleman cift sayi ise
            print('{} cift sayidir.'.format(i))
            if uceBolunen(i) == True:
                # listeden secilen eleman 3e tam bolunuyor ise
                print('{} 3 un katidir.'.format(i))
            elif beseBolunen(i) == True:
                # listeden secilen eleman 5e tam bolunuyor ise
                print('{} 5 in katidir.'.format(i))

sayiKontrol(1,20)
