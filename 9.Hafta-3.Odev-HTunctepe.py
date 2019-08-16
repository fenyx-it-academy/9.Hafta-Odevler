from functools import reduce


pzt = [ { 'isim': 'Fonksiyonlara calis', 'sure': 180, }, { 'isim': 'ornek coz', 'sure': 120, },
        { 'isim': 'odev kontrol','sure': 20, }, { 'isim': 'bayramlasma', 'sure': 200, }, ]

sali = [ { 'isim': 'gelecek haftaya hazirlik', 'sure': 240, }, { 'isim': 'ornek cozumlerine devam et', 'sure': 180, },
         { 'isim': 'kahve molasi', 'sure': 10, }, { 'isim': 'kitap oku', 'sure': 200, }, { 'isim': 'spor yap', 'sure': 40, }, ]


def scoreCounter(pzt, sali):
    mon = reduce(lambda score1, score2: score1+score2,
                 list(map(lambda score: round(score*20),
                          filter(lambda hfiltered: hfiltered >= 2,
                                 map(lambda hours: hours/60,
                                     map(lambda times: times['sure'], pzt))))))
    tue = reduce(lambda score1, score2: score1 + score2,
                 list(map(lambda score: round(score * 20),
                          filter(lambda hfiltered: hfiltered >= 2,
                                 map(lambda hours: hours / 60,
                                     map(lambda times: times['sure'], sali))))))

    return mon + tue



print('\nCalculated Score :', scoreCounter(pzt, sali))