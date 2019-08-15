def sayikontrol(ilksayi,sonsayi):

    def teksayi(sayi):
        if sayi in liste and sayi % 2 != 0:
            return sayi

    def ciftsayi(sayi):
        if sayi in liste and sayi % 2 == 0:
            return sayi

    def ucunkati(sayi):
        if sayi in liste and sayi % 3 == 0:
            return sayi

    def besinkati(sayi):
        if sayi in liste and sayi % 5 == 0:
            return sayi

    liste = list(range(ilksayi, sonsayi))
    for sayi in liste:
        #fonksiyonlari tek tek cagirdik
        if teksayi(sayi):
            print(sayi,"tek sayidir")
        if ciftsayi(sayi):
             print(sayi,"cift sayidir")
        if ucunkati(sayi):
            print(sayi,"ucun katidir")
        if besinkati(sayi):
            print(sayi,"besin katidir")

print(sayikontrol(1, 10))