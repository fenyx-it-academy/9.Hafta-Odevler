# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 17:20:26 2019

@author: HP
"""

#ODEV 3: 
#Map, filter ve reduce kullanarak yukarida belirtilen iki gunluk plan neticesinde 
#                                 kac puan kazanilacagini hesaplayan bir program yaziniz.
#•	Map ile sureleri saat cinsine donusturun.
#•	Iki saatin altindaki tum rutinleri filter ile eleyin. 
#•	Sureleri saatte 20 puan kazandiracak sekilde saatlik bazda guncelleyin. 
#•	Kusurlu degerleri .round() ile yuvarlayin. 
#•	Son olarak reduce ile kullanicinin kac puan kazandigini hesaplayin.



from functools import reduce

pzt = [{'isim': 'Fonksiyonlara calis', 'sure': 180 },
       {'isim': 'ornek coz','sure': 120 }, 
       {'isim': 'odev kontrol','sure': 20 },
       {'isim': 'bayramlasma','sure': 200}]

sali = [{'isim': 'gelecek haftaya hazirlik','sure':240},
        {'isim': 'ornek cozumlerine devam et','sure': 180}, 
        {'isim': 'kahve molasi','sure': 10},
        {'isim':'kitap oku','sure':200},
        {'isim':'spor yap','sure':40}]


pztsaat= list(filter(lambda f: f>=2,list(map(lambda a:a/60 , list(map(lambda x: x['sure'] ,pzt))))))
print(f'Pazartesi planlarin puani =',reduce(lambda x,y:x+y,list(map(lambda puan: round(puan*20),pztsaat))))

salisaat= list(filter(lambda f: f>=2,list(map(lambda a:a/60 , list(map(lambda x: x['sure'] ,sali))))))
print(f'Sali planlarin puani =',reduce(lambda x,y:x+y,list(map(lambda puan: round(puan*20),salisaat))))

print(f'Toplam Puan =',reduce(lambda x,y: x+y,list(map(lambda tum : round(tum*20), pztsaat+salisaat))))

# %% Genellestirilmis puanlama,,, Fonksiyon tanimlayarak!

from functools import reduce

pzt = [{'isim': 'Fonksiyonlara calis', 'sure': 180 },
       {'isim': 'ornek coz','sure': 120 }, 
       {'isim': 'odev kontrol','sure': 20 },
       {'isim': 'bayramlasma','sure': 200}]

sali = [{'isim': 'gelecek haftaya hazirlik','sure':240},
        {'isim': 'ornek cozumlerine devam et','sure': 180}, 
        {'isim': 'kahve molasi','sure': 10},
        {'isim':'kitap oku','sure':200},
        {'isim':'spor yap','sure':40}]

def gunpuan(gun):
    saat=list(filter(lambda f: f>=2,list(map(lambda dak: dak/60, list(map(lambda x:x['sure'],gun))))))
    puan=reduce(lambda a,b: a+b,list(map(lambda u : round(u*20),saat)))
    return puan

print('Pazartesi gunu puanlar toplami =',gunpuan(pzt), '\nSali Gunu puanlar toplami =',gunpuan(sali))
print("Pazartesi ve Sali gunleri puanlar toplami =", gunpuan(pzt+sali))



