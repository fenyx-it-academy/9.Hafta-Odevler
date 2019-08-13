#ODEV 2: Verilen bir sayi listesinin elemanlarindan tek olanlari ikiyle carpan ve
# hepsini toplayip sonucu veren bir fonksiyon yaziniz. Map, filter ve reduce kullaniniz.
from functools import reduce
def toplama(*liste):
#tek sayi girilmediginde liste bos oldugu icin hata verir
    return reduce( lambda a,b : (a+b) ,filter(lambda c:(c % 2),liste ))*2 +\
           reduce( lambda a,b : (a+b) ,filter(lambda c:(c % 2==0),liste ))    #cift olanlar toplaniyor
                     #tek olanlar 2 ile carpiliyor oyle toplaniyor
#---------------------------------------------------

print(toplama(2,4,6,123,44,12,54,66,33,7,88))



#---------------------------------------------------
#burada yukaridaki soruna cozum bulunmus tur
def fark(*sayilar):
    #tek sayilari ayiriyor
    ayikla=list(filter ( lambda c : c % 2==1 , map(lambda x:x , sayilar)))

    if ayikla==[]:   #liste bossa 0 donduruyor
        ayikla=[0]
     #tek sayilari ve listeyi topluyor boylece 2 ile carpmaya gerek yok
    return reduce(lambda x,y:x+y,map(lambda x:x,ayikla))+reduce(lambda x,y:x+y,map(lambda x:x,sayilar))
#-------------------------------------------------

print(fark(1,4,5,5,7,88,76))


