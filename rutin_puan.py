from functools import reduce

pzt = [
  {
    'isim': 'Fonksiyonlara calis',
    'sure': 180,
  },
  {
    'isim': 'ornek coz',
    'sure': 120,
  },
  {
    'isim': 'odev kontrol',
    'sure': 20,
  },
  {
    'isim': 'bayramlasma',
    'sure': 200,
  },
]

sali = [
  {
    'isim': 'gelecek haftaya hazirlik',
    'sure': 240,
  },
  {
    'isim': 'ornek cozumlerine devam et',
    'sure': 180,
  },
  {
    'isim': 'kahve molasi',
    'sure': 10,
  },
  {
    'isim': 'kitap oku',
    'sure': 200,
  },
  {
    'isim': 'spor yap',
    'sure': 40,
  },
]
toplam_puan=0
for gun in [pzt,sali]:
  #pzt ve sali icin dongu
  gunler=map(lambda x: round(x['sure']/60), gun)
  #gun icindeki sözlüklerin surelerin degerleri
  #60 a bolunup yaklsın degerileri ile liste olusturulur
  sureler=filter(lambda x: x>=2,gunler)
  #gunler listesi icindeki degerlerin 2 ve 2 den buyuk
  # olanları flitrelenir
  puanlar=map(lambda x: x*20 , sureler)
  #sureler listesindeki degerler 20 ile carpılır
  toplam_puan+=reduce(lambda x,y: x+y, puanlar)
  #puanlar listesindeki verilerin birikimli(cumulative)
  #toplamı hesaplanır
print (f'Toplam puan = {toplam_puan}')


#BU KODLARI BİRLEŞTİRİP TEK SATIR OLARAK DA YAZABİLİRİZ
toplam=reduce(lambda x,y: x+y, (map(lambda x: x*20, (filter(lambda x: x>=2,(map(lambda x: round(x['sure']/60), pzt+sali)))))))
print (f'Toplam puan = {toplam}')

