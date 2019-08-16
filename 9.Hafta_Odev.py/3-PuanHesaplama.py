"""pzt = [{'isim': 'Fonksiyonlara calis','sure': 180},
        {'isim': 'ornek coz','sure': 120},
        {'isim': 'odev kontrol','sure': 20},
        {'isim': 'bayramlasma','sure': 200}]

sali = [{'isim': 'gelecek haftaya hazirlik','sure': 240},
        {'isim': 'ornek cozumlerine devam et','sure': 180},
        {'isim': 'kahve molasi','sure': 10},
        {'isim': 'kitap oku','sure': 200},
        {'isim': 'spor yap','sure': 40}]

Not: Sureler dakika cinsindendir!

Map, filter ve reduce kullanarak yukarida belirtilen iki gunluk plan neticesinde kac puan kazanilacagini hesaplayan bir program yaziniz.

	•	Map ile sureleri saat cinsine donusturun.
	•	Iki saatin altindaki tum rutinleri filter ile eleyin.
	•	Sureleri saatte 20 puan kazandiracak sekilde saatlik bazda guncelleyin.
	•	Kusurlu degerleri .round() ile yuvarlayin.
	•	Son olarak reduce ile kullanicinin kac puan kazandigini hesaplayin.
	•	Degisken isimlerinin duzgun ve anlasilir olmasina ozen gosterin."""

pzt = [{'isim': 'Fonksiyonlara calis','sure': 180},
        {'isim': 'ornek coz','sure': 120},
        {'isim': 'odev kontrol','sure': 20},
        {'isim': 'bayramlasma','sure': 200}]

sali = [{'isim': 'gelecek haftaya hazirlik','sure': 240},
        {'isim': 'ornek cozumlerine devam et','sure': 180},
        {'isim': 'kahve molasi','sure': 10},
        {'isim': 'kitap oku','sure': 200},
        {'isim': 'spor yap','sure': 40}]



from functools import reduce

toplam_gun = pzt+sali

sure = filter(lambda x: x ['sure']>=120, toplam_gun)#filter ile 2 saat ve ustunu aldik
saat = list(map(lambda x: round(x['sure']/60)*20,sure))#dakika ile carpip yuvarladik
puan =reduce(lambda x, y : x + y, saat)
print(puan)
