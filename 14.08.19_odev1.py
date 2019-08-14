def sayikontrol():
    kucuk=int(input("Lutfen kucuk sayinizi giriniz : "))
    buyuk=int(input("Lutfen buyuk sayinizi giriniz : "))

    for i in range(kucuk, buyuk+1):
        if i % 2 != 0:
            print(i, "tek sayidir")
        if i % 2 == 0:
            print(i, "cift sayidir")
        if i % 3 == 0:
            print(i, "ucun katidir")
        if i % 5 == 0:
            print(i, "besin katidir")
    return "Islem basariyla tamamlandi"

print(sayikontrol())