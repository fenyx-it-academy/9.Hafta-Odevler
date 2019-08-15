pzt = [{ 'isim': 'Fonksiyonlara calis', 'sure': 180, },
        { 'isim': 'ornek coz', 'sure': 120, },
        { 'isim': 'odev kontrol', 'sure': 20, },
        { 'isim': 'bayramlasma', 'sure': 200, } ]

sali = [{ 'isim': 'gelecek haftaya hazirlik', 'sure': 240, },
         { 'isim': 'ornek cozumlerine devam et', 'sure': 180, },
         { 'isim': 'kahve molasi', 'sure': 10, },
         { 'isim': 'kitap oku', 'sure': 200, },
         { 'isim': 'spor yap', 'sure': 40, } ]


def saateCevir(gun):
    sure = gun['sure']

    saat = sure // 60
    gun['sure'] = saat

list(map(saateCevir, pzt))
list(map(saateCevir, sali))
#dakika cinsinde yazilan sureler saate cevrildi

ikiSaatUstu = lambda x: x['sure'] >= 2
pztIkiSaatUstu = list(filter(ikiSaatUstu, pzt))
saliIkiSaatUstu = list(filter(ikiSaatUstu, sali))
# filter ile sadece 2 saat uzeri olan rutinler bulundu

print('Pazartesi gunu 2 saat uzerindeki aktiviteler:',pztIkiSaatUstu)
print('Sali gunu 2 saat uzerindeki aktiviteler:',saliIkiSaatUstu)

from functools import reduce

toplamPuan = lambda x, y: x+y
sureler = []

for i in pztIkiSaatUstu:
    sureler.append(i['sure'])
    #ptesi iki saat uzerindeki aktiviteler sureler listesinde eklendi
for i in saliIkiSaatUstu:
    sureler.append(i['sure'])
    # sali iki saat uzerindeki aktiviteler sureler listesinde eklendi

print('Iki saat uzeri tum sureler:',sureler)
toplamPuanSonuc = reduce(toplamPuan, sureler)
#reduce ile sureler listesindeki elemanlar toplam puan fonskiyonu ile toplamdi

print('Toplam puan:',toplamPuanSonuc*20)
