from functools import reduce
pzt = [ { "isim": 'Fonksiyonlara calis', "sure": 180 }, { "isim": 'ornek coz', "sure": 120 },
        { "isim": 'odev kontrol', "sure": 20 }, { "isim": 'bayramlasma', "sure": 200 } ]
sali = [ { "isim": 'gelecek haftaya hazirlik', "sure": 240}, { "isim": 'ornek cozumlerine devam et', "sure": 180},
         { "isim": 'kahve molasi', "sure": 10}, { "isim": 'kitap oku', "sure": 200}, { "isim": 'spor yap', "sure": 40} ]
pzt_puan = reduce(lambda a,b:a+b, list(map(lambda a: round(a*20),filter(lambda a: a>=2,map(lambda a: a["sure"]/60, pzt)))))
sali_puan = reduce(lambda a,b:a+b, list(map(lambda a: round(a*20),filter(lambda a: a>=2,map(lambda a: a["sure"]/60, sali)))))

print(pzt_puan + sali_puan)

