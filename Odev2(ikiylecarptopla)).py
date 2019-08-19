##ODEV 2: Verilen bir sayi listesinin elemanlarindan tek olanlari ikiyle carpan
##ve hepsini toplayip sonucu veren bir fonksiyon yaziniz. Map, filter ve reduce
##kullaniniz.
from functools import reduce
liste=[5,8,6,12,9,7,32,6,4,5,2,5,12]
def teksayi(deger):
    teksayiliste=reduce(lambda sayi1,sayi2:sayi1+sayi2,list(map(lambda x:x*2,filter(lambda y:y%2==1,deger))))
                  #reduce ile toplam bulundu\map ile tek sayilar iki ile carpildi\filter ile tek sayilar ayiklandi.  
    ciftsayiliste=reduce(lambda sayi1,sayi2:sayi1+sayi2,list(filter(lambda z:z%2==0,deger)))
                  #reduce ile sayilar toplandi\ filter ile cift sayilar ayiklandi. 
    return ciftsayiliste+teksayiliste

print("Toplam:", teksayi(liste))
