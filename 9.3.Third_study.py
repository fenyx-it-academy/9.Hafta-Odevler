print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


from functools import reduce

pzt = [{'isim': 'Fonksiyonlara calis', 'sure': 180}, {'isim': 'ornek coz', 'sure': 120},
       {'isim': 'odev kontrol', 'sure': 20}, {'isim': 'bayramlasma', 'sure': 200}]

sali = [{'isim': 'gelecek haftaya hazirlik', 'sure': 240}, {'isim': 'ornek cozumlerine devam et', 'sure': 180},
        {'isim': 'kahve molasi', 'sure': 10}, {'isim': 'kitap oku', 'sure': 200}, {'isim': 'spor yap', 'sure': 40}]

monday = reduce(lambda a, b: a + b, list(
        map(lambda z: round(z * 20), filter(lambda y: y >= 2, map(lambda t: t / 60, map(lambda x: x['sure'], pzt))))))
tuesday = reduce(lambda a, b: a + b, list(
        map(lambda z: round(z * 20), filter(lambda y: y >= 2, map(lambda t: t / 60, map(lambda x: x['sure'], sali))))))


def total_earn(m, t):
    return print(m + t)


total_earn(monday, tuesday)


#Burada pazartesi ve sali gunu icindeki rakamlari cekmek onemli onuda asagidaki ensonda map fonksiyonuyla value cekerek elde edildi!!!
# monday = reduce(lambda a, b: a+b, list(map(lambda z: round(z*20), filter(lambda y: y >= 2, map(lambda t: t/60, map(lambda x: x['sure'], pzt))))))
# tuesday = reduce(lambda a, b: a+b, list(map(lambda z: round(z*20), filter(lambda y: y >= 2, map(lambda t: t/60, map(lambda x: x['sure'], sali))))))



