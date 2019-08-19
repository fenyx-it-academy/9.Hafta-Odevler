pzt = [ { "isim": 'Fonksiyonlara calis', "sure": 180, }, { "isim": 'ornek coz', "sure": 120, }, { "isim": 'odev kontrol', "sure": 20, }, { "isim": 'bayramlasma', "sure": 200, }, ]
sali = [ { "isim": 'gelecek haftaya hazirlik', "sure": 240, }, { "isim": 'ornek cozumlerine devam et', "sure": 180, },{ "isim": 'kahve molasi', "sure": 10, },
         { "isim": 'kitap oku', "sure": 200, }, { "isim": 'spor yap', "sure": 40, }, ]

a=reduce(lambda sayi1,sayi2:sayi1+sayi2,list(filter(lambda sayi:sayi>2,list(map(lambda sozluk:round(sozluk["sure"]/60),pzt)))))
# Map ile sureler saat cinsinden yuvarlandi
# Filter ile saat 2den buyuk ise degerler filtrelendi
# Reduce ile 2den buyuk tum sureler toplandi
b=reduce(lambda sayi1,sayi2:sayi1+sayi2,list(filter(lambda sayi:sayi>2,list(map(lambda sozluk:round(sozluk["sure"]/60),sali)))))
print("Toplam puan:",(a+b)*20)   # Toplam puan icin toplam sure 20 ile carpildi
