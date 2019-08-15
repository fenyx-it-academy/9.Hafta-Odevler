from functools import reduce

pzt =[
{'isim':'Fonksiyonlara calis','sure': 180 },
{'isim': 'ornek coz','sure': 120},
{'isim': 'odev kontrol','sure': 20 },
{'isim': 'bayramlasma','sure': 200 }
      ]

sali = [
{'isim': 'gelecek haftaya hazirlik','sure': 240 },
{'isim': 'ornek cozumlerine devam et','sure': 180},
{'isim': 'kahve molasi','sure': 10},
{'isim': 'kitap oku','sure': 200},
{'isim': 'spor yap','sure':40 }
        ]


# print(list(map(lambda x:x/60, (i["sure"] for i in pzt))))

# a = list(filter(lambda x:x>=2,map(lambda x:x/60, (i["sure"] for i in pzt))))
#
# b = list(filter(lambda x:x>=2,map(lambda x:x/60, (i["sure"] for i in sali))))

a = list(map(lambda x : round(x*20),filter(lambda x:x>=2,map(lambda x:x/60, (i["sure"] for i in sali)))))   #roundu islem yaptigimiz ksiimda yazabilioruz

b = list(map(lambda x : round(x*20),filter(lambda x:x>=2,map(lambda x:x/60, (i["sure"] for i in pzt)))))


print(reduce(lambda x,y : x+y,a+b)) # yukarida a ve b degiskenini tanimlamak zorunda kaldik.

#Yaptigimiz her yeni islemde alt satira gecip "map" fonksiyonu ile islemi yazip ikinci argumana bir ust satiri aliriz.


# toplam=[]     #Buda yukaridaki asamanin ikinci farkli yapilabilecek sekli..=)
# 
# for i in a:
#     i*=20
#     toplam.append(i)
#
#
# for i in b:
#     i*=20
#     toplam.append(i)
#
# print(toplam)



