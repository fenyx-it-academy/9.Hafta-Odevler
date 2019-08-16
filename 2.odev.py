##ODEV 2:
##Verilen bir sayi listesinin elemanlarindan tek olanlari ikiyle
##carpan ve hepsini toplayip sonucu veren bir fonksiyon yaziniz.
##Map, filter ve reduce kullaniniz.

##def fonk(deger):
##    Tek=[]
##    hesap=[]
##    toplam = 0
##    for i in deger:
##        if i % 2 != 0:
##            Tek += [i]
##    print("Tek ",Tek)
##       
##    for i in Tek:
##        hesap += [(int(i)*2)]
##    print("hesap ",hesap)
##    
##    for i in hesap:
##        toplam += int(i)
##    print("toplam ",toplam)
##    return toplam
##fonk(range(10))

kasa=[5,7,8,15]
ayir=list(filter(lambda x: x%2!=0, kasa))
carp=list(map(lambda y: (y*2), ayir))

print(ayir)
print(carp)
print(sum(carp))
