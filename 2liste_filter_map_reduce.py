# Verilen bir sayi listesinin elemanlarindan tek olanlari ikiyle carpan ve
# hepsini toplayip sonucu veren bir fonksiyon yaziniz.
# Map, filter ve reduce kullaniniz.
from functools import reduce
def toplam():
    liste=[1,1,2,3,4,5,6,8,7,9,10,12,13,14,17,18,11,55,23,3,6,44,76]
    print(reduce(lambda x,y:x+y,map(lambda x:x*2,list(filter(lambda x: x % 2 != 0, liste)))))
toplam()
