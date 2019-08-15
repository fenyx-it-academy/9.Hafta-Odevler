from functools import reduce
pzt =[
{'isim':'Fonksiyonlara calis','sure': 180 },
{'isim': 'ornek coz','sure': 120},
{'isim': 'odev kontrol','sure': 20 },
{'isim': 'bayramlasma','sure': 200 }]
sali = [
{'isim': 'gelecek haftaya hazirlik','sure': 240 },
{'isim': 'ornek cozumlerine devam et','sure': 180},
{'isim': 'kahve molasi','sure': 10},
{'isim': 'kitap oku','sure': 200},
{'isim': 'spor yap','sure':40 }]
#listelerdeki sureleri reduce ile kullanabilmek icin yeni listelere tanimladik
#bu listelerde once listelerdeki sureleri aldik ve bunu saat haline donusturduk
#saat halleri 2 saatten az olanlari filter ile eledik ve bunlari puanlama icin
#20 ile carptik ve kusurattan kurtulmak icin round kullandik
puansali=list(map(lambda x:round(x*20),filter(lambda x:x>=2,(map(lambda x:x/60,(i['sure']for i in sali))))))
puanpzt=list(map(lambda x:round(x*20),filter(lambda x:x>=2,(map(lambda x:x/60,(i['sure']for i in pzt))))))
#yukarida elde ettigmiz puanlari reduce ile topladik ve bunu kullaniciya sunduk
print(reduce(lambda x,y:x+y,puansali+puanpzt))