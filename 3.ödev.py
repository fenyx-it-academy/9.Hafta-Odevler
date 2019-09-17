from functools import reduce
pzt = [ { 'isim': 'Fonksiyonlara calis', 'sure': 180 }, { 'isim': 'ornek coz', 'sure': 120 }, { 'isim': 'odev kontrol', 'sure': 20 }, { 'isim': 'bayramlasma', 'sure': 200 } ]

sali = [ { 'isim': 'gelecek haftaya hazirlik', 'sure': 240 }, { 'isim': 'ornek cozumlerine devam et', 'sure': 180 }, { 'isim': 'kahve molasi', 'sure': 10 }, { 'isim': 'kitap oku', 'sure': 200 }, { 'isim': 'spor yap', 'sure': 40 } ]

saat=list(map(lambda x : x["sure"]/60,pzt))                          # herbir dakikanın saate çevrilmesi
print(saat)
ikiden_fazla=list(filter(lambda time: time>2 , saat))             # 2 saatten fazla olanların seçilmesi
print(ikiden_fazla)
puanlar=list(map(lambda a: a*20,ikiden_fazla))                  # seçilen saatlerin 20 puan ile çarpılması
print(puanlar)
yuvarlanmış=map(lambda r: round(r),puanlar)                   # rounda yuvarlanması
print(yuvarlanmış)
