print('b.')
'''
ODEV 3: pzt = [ { isim: 'Fonksiyonlara calis', sure: 180, }, { isim: 'ornek coz', sure: 120, }, { isim: 'odev kontrol', sure: 20, }, { isim: 'bayramlasma', sure: 200, }, ]

sali = [ { isim: 'gelecek haftaya hazirlik', sure: 240, }, { isim: 'ornek cozumlerine devam et', sure: 180, }, { isim: 'kahve molasi', sure: 10, }, { isim: 'kitap oku', sure: 200, }, { isim: 'spor yap', sure: 40, }, ]

Not: Sureler dakika cinsindendir!

Map, filter ve reduce kullanarak yukarida belirtilen iki gunluk plan neticesinde 
kac puan kazanilacagini hesaplayan bir program yaziniz.

•	Map ile sureleri saat cinsine donusturun.
•	Iki saatin altindaki tum rutinleri filter ile eleyin. 
•	Sureleri saatte 20 puan kazandiracak sekilde saatlik bazda guncelleyin. 
•	Kusurlu degerleri .round() ile yuvarlayin. 
•	Son olarak reduce ile kullanicinin kac puan kazandigini hesaplayin.
•	Degisken isimlerinin duzgun ve anlasilir olmasina ozen gosterin.
'''
from functools import reduce

pzt = [ { 'isim': 'Fonksiyonlara calis', 'sure': 180, }, { 'isim': 'ornek coz', 'sure': 120, },
        { 'isim': 'odev kontrol','sure': 20, }, { 'isim': 'bayramlasma', 'sure': 200, }, ]

sali = [ { 'isim': 'gelecek haftaya hazirlik', 'sure': 240, }, { 'isim': 'ornek cozumlerine devam et', 'sure': 180, },
         {'isim':'kahve molasi','sure':10, }, {'isim':'kitap oku','sure': 200, },{ 'isim': 'spor yap', 'sure': 40, }, ]
# sureleri listede tutmak icin bos bir liste tanimladik
liste_pzt=[]
liste_sali=[]
# for dongusunu kullanarak sureleri bos listelerimize ekledik
for i in range(len(pzt)):
    liste_pzt.append(pzt[i]['sure'])
for i in range(len(sali)):
    liste_sali.append(sali[i]['sure'])

#list(map(lambda x:round(x/60,1),liste_pzt)  dakikalari saate cevirdik.round ile yuvarlama yaptik...listeye donusturduk
# list(filter(lambda t:t>= 2,....) filter ile 2 saat ustundekileri sectik
# list(map(lambda a:round(a*20)....) 20 ile carptik....round ile yuvarlama islemini yaptik
# list(map(lambda k:round(k),....) yuvarlama islemini yaptik
# reduce(lambda b,r:b+r,....) reduce ile topladik

pzt_t_puan=reduce(lambda b,c:b+c,list(map(lambda a:round(a*20),list(filter(lambda t:t>= 2,list(map(lambda x:round(x/60,1),liste_pzt)))))))
sali_t_puan=reduce(lambda b,c:b+c,list(map(lambda a:round(a*20),list(filter(lambda t:t>= 2,list(map(lambda x:round(x/60,1),liste_sali)))))))
print('toplam puan :',pzt_t_puan+sali_t_puan)

# buda tek satirda yazilmis hali
#print('toplam puan :',reduce(lambda b,c:b+c,list(map(lambda a:round(a*20),list(filter(lambda t:t>= 2,list(map(lambda x:round(x/60,1),liste_pzt))))))) + reduce(lambda b,c:b+c,list(map(lambda a:round(a*20),list(filter(lambda t:t>= 2,list(map(lambda x:round(x/60,1),liste_sali))))))))
