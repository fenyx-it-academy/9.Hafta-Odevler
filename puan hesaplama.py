
pzt=[{'isim':'Fonksiyonlara calis','sure':180},
     {'isim':'ornek coz','sure':120},
     {'isim':'odev kontrol','sure':20},
     {'isim':'bayramlasma','sure':200}]

sali=[{'isim':'gelecek haftaya hazirlik','sure': 240},
      {'isim':'ornek cozumlerine devam et','sure':180},
      {'isim':'kahve molasi','sure':10},
      {'isim':'kitap oku','sure':200},
      {'isim':'spor yap','sure':40}]

pzt.extend(sali)
#salinin elemanlarini da pzt listesi icine atti


saatdonusum=map(lambda x:x['sure']/60,pzt)
#surelerin saate donusturulmus halindan liste olusturdu.


ikisaattenfazla=filter(lambda x:x>=2,saatdonusum)
#saat cinsinde 2 ve 2 saaten fazla olanlarin listesi olusturuldu.


puan=map(lambda x:x*20,ikisaattenfazla)
#saat basina 20 puan verildi


puan_yuvarla=map(lambda x:round(x),puan)
#puanlamadan sonra sayida yuvarlama yapildi.

from functools import reduce
#reduce calistirmak icin import etti

toplam_puan=reduce(lambda x,y:x+y,puan_yuvarla)
#yuvarlama yapilmis puanlarin hepsi toplandi

#bu islem tek satirda birlestirilebilir



print(toplam_puan)








