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


print(reduce(lambda x,y:x+y,list(map(lambda x:round(x),list(map(lambda x:x*20,list(filter(lambda x:x>=2,list(map(lambda x:x/60,list(map(lambda x:x['sure'],pzt+sali))))))))))))