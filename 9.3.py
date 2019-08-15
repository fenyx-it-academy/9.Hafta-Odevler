monday = [ { 'isim': 'Fonksiyonlara calis', 'sure': 180, },
        { 'isim': 'ornek coz', 'sure': 120, },
        { 'isim': 'odev kontrol','sure': 20, },
        { 'isim': 'bayramlasma', 'sure': 200, }, ]

tuesday= [ { 'isim': 'gelecek haftaya hazirlik', 'sure': 240, },
         { 'isim': 'ornek cozumlerine devam et', 'sure': 180, },
         { 'isim': 'kahve molasi', 'sure': 10, },
         { 'isim': 'kitap oku', 'sure': 200, },
         { 'isim': 'spor yap', 'sure': 40, }, ]

from functools import reduce

sum=monday+tuesday
points=reduce(lambda x, y : x + y, list(map(lambda x: round(x['sure']/60)*20,filter(lambda x: x ['sure']>=120, sum))))

print(points)