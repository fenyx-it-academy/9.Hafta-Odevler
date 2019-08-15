from functools import reduce

pzt = [ { "isim": 'Fonksiyonlara calis', "sure": 180, },
        { "isim": 'ornek coz', "sure": 120, },
        { "isim": 'odev kontrol', "sure": 20, },
        { "isim": 'bayramlasma', "sure": 200, } ]

sali = [ { "isim": 'gelecek haftaya hazirlik', "sure": 240, },
         { "isim": 'ornek cozumlerine devam et', "sure": 180, },
         { "isim": 'kahve molasi', "sure": 10, },
         { "isim": 'kitap oku', "sure": 200, },
         { "isim": 'spor yap', "sure": 40, } ]

sum_days = pzt + sali

#to convert to hour:
time = list(map(lambda item: item["sure"] / 60, sum_days))
#filter them below 2 hour:
time = list(filter(lambda item: item >= 2, time))
#to calculate their point as one hour is 20 point:
point = list(map(lambda item: round(item * 20), time))
#sum all the points:
point = reduce(lambda item1, item2: item1 + item2, point)


print(point)
