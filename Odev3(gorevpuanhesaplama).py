##ODEV 3: pzt = [ { 'isim': 'Fonksiyonlara calis', 'sure': 180 },
##                { 'isim': 'ornek coz', 'sure': 120 },
##                { 'isim': 'odev kontrol', 'sure': 20 },
##                { 'isim': 'bayramlasma', 'sure': 200 } ]
##
##sali = [ { 'isim': 'gelecek haftaya hazirlik', 'sure': 240 },
##         { 'isim': 'ornek cozumlerine devam et', 'sure': 180 },
##         { 'isim': 'kahve molasi', 'sure': 10 },
##         { 'isim': 'kitap oku', 'sure': 200 },
##         { 'isim': 'spor yap', 'sure': 40 } ]
##
##Not: Sureler dakika cinsindendir!
##
##Map, filter ve reduce kullanarak yukarida belirtilen iki gunluk plan
##neticesinde kac puan kazanilacagini hesaplayan bir program yaziniz.
##
##•	Map ile sureleri saat cinsine donusturun.
##•	Iki saatin altindaki tum rutinleri filter ile eleyin. 
##•	Sureleri saatte 20 puan kazandiracak sekilde saatlik bazda guncelleyin. 
##•	Kusurlu degerleri .round() ile yuvarlayin. 
##•	Son olarak reduce ile kullanicinin kac puan kazandigini hesaplayin.
##•	Degisken isimlerinin duzgun ve anlasilir olmasina ozen gosterin.
##

from functools import reduce

pzt = [ { "isim": 'Fonksiyonlara calis', "sure": 180, },
        { "isim": 'ornek coz', "sure": 120, },
        { "isim": 'odev kontrol', "sure": 20, },
        { "isim": 'bayramlasma', "sure": 200, },]
sali = [ { "isim": 'gelecek haftaya hazirlik', "sure": 240, },
         { "isim": 'ornek cozumlerine devam et', "sure": 180, },
         { "isim": 'kahve molasi', "sure": 10, },
         { "isim": 'kitap oku', "sure": 200, },
         { "isim": 'spor yap', "sure": 40, },]

pazartesi=reduce(lambda sayi1,sayi2:sayi1+sayi2,list(filter(lambda saat:saat>=2,list(map(lambda zaman:round(zaman["sure"]/60),pzt)))))
# reduce ile toplam zaman saat turunden bulundu\ filter ile 2 saatin alti ayiklandi \ map ile dakika olan sure saate cevrildi.

sali1= reduce(lambda sayi1,sayi2:sayi1+sayi2,list(filter(lambda saat:saat>=2,list(map(lambda zaman:round(zaman["sure"]/60),sali)))))

print("Toplam puaniniz:",(pazartesi+sali1)*20)
# toplam sure 20 ile carpildi cunku her saat 20 puan degerinde.


