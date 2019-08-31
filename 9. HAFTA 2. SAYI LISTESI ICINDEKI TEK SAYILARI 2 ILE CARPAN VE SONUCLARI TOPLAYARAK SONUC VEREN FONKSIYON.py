# Verilen bir sayi listesinin elemanlarindan tek olanlari ikiyle carpan ve
# hepsini toplayip sonucu veren bir fonksiyon yaziniz.
# Map, filter ve reduce kullaniniz.
from functools import reduce
def toplam():
    liste=[1,41,22,13,34,57,26,87,75,99,510,102,613,14,17,118,911,555,23,3,56,44,76]
    print(reduce(lambda x,x2:x+x2,map(lambda x:x*2,list(filter(lambda x: x % 2 != 0, liste))))) #Burada icten disa dogru bizden istenenleri uyguladik
toplam()
