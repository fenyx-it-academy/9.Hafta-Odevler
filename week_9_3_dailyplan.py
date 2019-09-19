from functools import reduce

mon = [{"isim": 'Fonksiyonlara calis', "sure": 180, }, {"isim": 'ornek coz', "sure": 120},
       {"isim": 'odev kontrol', "sure": 20, }, {"isim": 'bayramlasma', "sure": 200, }, ]
tue = [{"isim": 'gelecek haftaya hazirlik', "sure": 240, }, {"isim": 'ornek cozumlerine devam et', "sure": 180, },
        {"isim": 'kahve molasi', "sure": 10, }, {"isim": 'kitap oku', "sure": 200, },
        {"isim": 'spor yap', "sure": 40, }]

a = reduce(lambda number1, number2: number1 + number2,
           list(filter(lambda number: number > 2, list(map(lambda sozluk: round(sozluk["sure"] / 60), mon)))))
b = reduce(lambda number1, number2: number1 + number2,
           list(filter(lambda number: number > 2, list(map(lambda sozluk: round(sozluk["sure"] / 60), tue)))))

print("Total:", (a + b) * 20)
