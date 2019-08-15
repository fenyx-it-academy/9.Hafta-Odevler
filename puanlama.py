# ODEV 3: pzt = [ { isim: 'Fonksiyonlara calis', sure: 180, }, { isim: 'ornek coz', sure: 120, },
# { isim: 'odev kontrol', sure: 20, }, { isim: 'bayramlasma', sure: 200, }, ]
#
# sali = [ { isim: 'gelecek haftaya hazirlik', sure: 240, },
# { isim: 'ornek cozumlerine devam et', sure: 180, }, { isim: 'kahve molasi', sure: 10, },
# { isim: 'kitap oku', sure: 200, }, { isim: 'spor yap', sure: 40, }, ]
#
# Not: Sureler dakika cinsindendir!
#
# Map, filter ve reduce kullanarak yukarida belirtilen
# iki gunluk plan neticesinde kac puan kazanilacagini hesaplayan bir program yaziniz.
#
# •	Map ile sureleri saat cinsine donusturun.
# •	Iki saatin altindaki tum rutinleri filter ile eleyin.
# •	Sureleri saatte 20 puan kazandiracak sekilde saatlik bazda guncelleyin.
# •	Kusurlu degerleri .round() ile yuvarlayin.
# •	Son olarak reduce ile kullanicinin kac puan kazandigini hesaplayin.
# •	Degisken isimlerinin duzgun ve anlasilir olmasina ozen gosterin.
from functools import reduce
pzt = [ { 'isim': 'Fonksiyonlara calisma',      'sure': 180, },
        { 'isim': 'ornek cozme',                'sure': 120, },
        { 'isim': 'odev kontrol etme',          'sure': 20,  },
        { 'isim': 'bayramlasma',                'sure': 200, }, ]

sali = [{ 'isim': 'gelecek haftaya hazirlik',   'sure': 240, },
        { 'isim': 'ornek cozumlerine devam  ',  'sure': 180, },
        { 'isim': 'kahve molasi',               'sure': 10,  },
        { 'isim': 'kitap oku',                  'sure': 200, },
        { 'isim': 'spor yap',                   'sure': 40,  }, ]


def puanlama(liste):


    eleme=list(
    filter(lambda iki_saat:iki_saat if iki_saat > 119  #2 saati ayirma
    else 0,map(lambda liste_sure:liste_sure['sure'] ,liste))
    )   #listeyi aktarma

    #[round yuvarlama],[reduce toplama],[map ile sayi*20/60 yapilarak saat basi 20 puan yapildi]
    return round(reduce(lambda x,y:x+y,(map(lambda puan_ayar:puan_ayar*20/60,eleme))))




print('pazartesi puani (2 saat alti haric)',puanlama(pzt))
print('sali puani (2 saat alti haric)',puanlama(sali))
print('toplam puani (2 saat alti haric)',puanlama(sali)+puanlama(pzt))
