##ODEV 2: Verilen bir sayi listesinin elemanlarindan tek olanlari
# ikiyle carpan ve hepsini toplayip sonucu veren bir fonksiyon yaziniz.
# Map, filter ve reduce kullaniniz.

from functools import reduce
sayi=range(1,100)
sonuc=reduce(lambda sayi1,sayi2:sayi1+sayi2,list(map(lambda sayi:sayi*2,list(filter(lambda sayi:sayi%2 != 0,sayi)))))

print("Listedeki tek sayilarin iki ile carpilip toplanmis hali: ", sonuc)
