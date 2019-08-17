# teksayi = lambda x: x%2 != 0  # Tekssayi kontrolu fonksiyonu
def tek(x):
    if x%2 != 0:
        return x,"tek sayidir."

# ciftsayi= lambda sayi:sayi%2 ==0  # Ciftsayi kont. yapan fonk.
def cift(x):
    if x%2 == 0:
        return x,"cift sayidir."

# ucebol= lambda sayi: sayi%3 ==0  # Uce Bolunme
def ucebol(x):
    if x%3 == 0:
        return x,"3'e bolunur."

# besebol= lambda sayi: sayi%5 ==0  # 5e bolunme
def besebol(x):
    if x%5 == 0:
        return x,"5'e bolunebilir."
yeni=[tek,cift,ucebol,besebol]

def execute(x):  #yukarida yazdigimiz fonksiyonlari cagiran fonksiyonumuzu yaziyoruz.
    baslangic=int(input("Ilkdeger:"))
    bitis= int(input("sondeger:"))
    liste = list(range(baslangic,bitis))
    for i in liste:
        deger=list(map(lambda x:x(i),yeni))
        wdeger=list(filter(lambda x:x!=None,deger))
        for i in wdeger:
            for j in i:
                print(j,sep="")

execute(1)
