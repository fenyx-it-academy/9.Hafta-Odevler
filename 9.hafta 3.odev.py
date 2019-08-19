##ODEV 3: pzt = [ { isim: 'Fonksiyonlara calis', sure: 180, },
##                { isim: 'ornek coz', sure: 120, },
##                { isim: 'odev kontrol', sure: 20, },
##                { isim: 'bayramlasma', sure: 200, }, ]
##sali = [ { isim: 'gelecek haftaya hazirlik', sure: 240, },
##         { isim: 'ornek cozumlerine devam et', sure: 180, },
##         { isim: 'kahve molasi', sure: 10, },
##         { isim: 'kitap oku', sure: 200, },
##         { isim: 'spor yap', sure: 40, }, ]
##Not: Sureler dakika cinsindendir!
##Map, filter ve reduce kullanarak yukarida belirtilen
##iki gunluk plan neticesinde kac puan kazanilacagini
##hesaplayan bir program yaziniz.
##•	Map ile sureleri saat cinsine donusturun.
##•	Iki saatin altindaki tum rutinleri filter ile eleyin. 
##•	Sureleri saatte 20 puan kazandiracak sekilde saatlik bazda guncelleyin. 
##•	Kusurlu degerleri .round() ile yuvarlayin. 
##•	Son olarak reduce ile kullanicinin kac puan kazandigini hesaplayin.
##•	Degisken isimlerinin duzgun ve anlasilir olmasina ozen gosterin.

pzt=[{'isim':'Fonksiyonlara calis', 'sure': 180,},
     {'isim':'ornek coz', 'sure': 120,},
     {'isim':'odev kontrol', 'sure': 20,},
     {'isim':'bayramlasma', 'sure': 200,},]
sali=[{'isim':'gelecek haftaya hazirlik', 'sure': 240,},
      {'isim':'ornek cozumlerine devam et', 'sure': 180,},
      {'isim':'kahve molasi', 'sure': 10,},
      {'isim':'kitap oku', 'sure': 200,},
      {'isim':'spor yap', 'sure': 40,},]
liste=pzt+sali
print(liste,"\n")
print("Bu listeye gore iki gunluk ve her saatini 20 puandan toplam \nkazanilan puani hesap edersek...\n")
from functools import reduce
###reduce ile iki parametre girerek 60dkyi 20 puan sayarak tum surelerin toplamina
###gore kazanilan toplam puan map ile 20yle carpip 60a bolunerek bulunur.
islem1=list(filter(lambda x:x>=120,map(lambda x:x['sure'],liste)))
islem2=reduce(lambda x,y:x+y,list(map(lambda x:round(x),(map(lambda x:x*20/60,islem1)))))

print("Pazartesi ve Sali Toplam Kazanilan Puan: ",islem2)
            









