"""Verilen bir sayi listesinin elemanlarindan tek olanlari ikiyle carpan ve hepsini toplayip sonucu veren bir fonksiyon yaziniz. Map, filter ve reduce kullaniniz."""
from functools import reduce

fonksiyon = list(filter(lambda x: x % 2 != 0, [1, 3, 4, 2, 7, 5, 9]))#filter ile tek olanlari aldik
yenifonksiyon = list(map(lambda x: x * 2, fonksiyon))#map vasitasiyla 2 ile carptik
sonhali = reduce(lambda x, y: x + y, yenifonksiyon)#reduce ile topladik
print(sonhali)

