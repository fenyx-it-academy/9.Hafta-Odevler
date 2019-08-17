pzt = [ {'isim':'Fonksiyonlara calis','sure':180,},{ 'isim': 'ornek coz', 'sure': 120, },
        { 'isim': 'odev kontrol', 'sure': 20, },{ 'isim': 'bayramlasma','sure': 200, } ]
sali = [ { 'isim': 'gelecek haftaya hazirlik', 'sure': 240, },
         { 'isim': 'ornek cozumlerine devam et', 'sure': 180, },
         { 'isim': 'kahve molasi', 'sure': 10, }, { 'isim': 'kitap oku', 'sure': 200, },
         { 'isim': 'spor yap', 'sure': 40, } ]
# Not: Sureler dakika cinsindendir!
# Map, filter ve reduce kullanarak yukarida belirtilen iki gunluk plan neticesinde
# kac puan kazanilacagini hesaplayan bir program yaziniz.
# •	Map ile sureleri saat cinsine donusturun.
# •	Iki saatin altindaki tum rutinleri filter ile eleyin.
# •	Sureleri saatte 20 puan kazandiracak sekilde saatlik bazda guncelleyin.
# •	Kusurlu degerleri .round() ile yuvarlayin.
# •	Son olarak reduce ile kullanicinin kac puan kazandigini hesaplayin.
# •	Degisken isimlerinin duzgun ve anlasilir olmasina ozen gosterin.
lis=[pzt,sali] #Listelerimizi tek bir listeye ekledik.
yeni=[]
for i in lis:   #burada listelerimizin icindeki sure degerleriniayiklamak icin
    for k in i:     #actigimiz listelerin kademe kademe derinine inerek buldugumuz degerleri
        for j in k.values():    #yeni bir dosyaya kaydettirk.
            yeni.append(j)

yemsyeni=(list(filter(lambda x:type(x)==int,yeni)))     #yeni dosyamizda sadece sure degerlerini filtreledik.
print("Bir kisimin ptsi ve sali gunu aktivitelerinin sure listesi su sekildedir.:\n",yemsyeni)
from functools import reduce        #bundan sonra kisinin aktiviteleri ile yaptigi puani hesaplayan
                                    #fonksiyonumuzu yaziyoruz.
print("Kisinin bu aktiviteleri sonucu kazandigi puan:\n",
      (reduce(lambda x,y:x+y,(map(lambda x:(x*20).__round__(),
                                  (filter(lambda x:x>=2,(map(lambda x:x/60,yemsyeni)))))))))

