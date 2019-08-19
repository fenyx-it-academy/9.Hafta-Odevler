##ODEV 2: Verilen bir sayi listesinin elemanlarindan tek olanlari
##ikiyle carpan ve hepsini toplayip sonucu veren bir fonksiyon yaziniz.
##Map, filter ve reduce kullaniniz.

###reduce kullanarak onceden olusturulan listeden iki
###parametre girerek ve filtreleyerek bu islemi saglayalim...
liste=[2,3,4,6,7,8,12,33,48,71,108]

print("""
Asagidaki listenin icindeki tek sayilari
ikiyle carpip diger sayilarla toplamini
ariyoruz: \n\n""",
liste,"\n")
        

from functools import reduce
sonuc=reduce (lambda x,y:x+y,list(map(lambda x: x*2,list(filter(lambda x:x%2==1, liste)))))
print("İslemin sonucu=",sonuc)
