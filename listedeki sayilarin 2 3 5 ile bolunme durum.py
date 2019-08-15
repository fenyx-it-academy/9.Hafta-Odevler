#tek sayi kontrolu yapan fonksiyon.

def teksayi_kontrol(sayi):
    if int(sayi)%2==1:              #argumentin integer hali 2 ye tam bolunmuyorsa
        return " tek sayidir"
    return ""

#cift sayi kontrolu yapan fonksiyon

def cifsayi_kontrol(sayi):
    if int(sayi)%2==0:              #argumentin integer hali 2 ye tam bolunuyorsa
        return " cift sayidir"
    return ""
#3 un kati olanlari kontrol eden fonksiyon

def ucunkati(sayi):
    if int(sayi)%3==0:                  #argumentin integer hali 3 e tam bolunuyorsa
       return " 3 un katidir"
    return ""

#5in kati olanlari kontrol eden fonksiyon

def besinkati(sayi):
    if int(sayi)%5==0:                  #argumentin integer hali 5 e tam bolunuyorsa
        return " 5 in katidir"
    return ""

#sayi araligi icin ilk sayiyi sayi olarak kullanicidan alma
def ilk():
    while True:
        ilksayi = input("sayi araligi icin baslangic sayisini giriniz:")
        if ilksayi.isdigit():
            break
        else:
            "gecersiz ifade girdiniz"
    return ilksayi


#sayi araligi icin son sayiyi sayi olarak kullanicidan alma
def son():
    while True:
        sonsayi = input("sayi araligi icin son sayiyi giriniz:")
        if sonsayi.isdigit():
            break
        else:
            "gecersiz ifade girdiniz"
    return sonsayi



#ilk sayi ve son sayidan aralik olusturup bu sayilarin durumunu inceleme
def sayikontrol():
    a=int(ilk())                        #ilk sayiyi olusturmaya calisacak
    while True:
        b=int(son())                    #son sayiyi olusturmaya calisacak
        if a<b:                         #son sayi ilk sayidan buyuk olmali
            for i in range(a,b):
                durum=teksayi_kontrol(i)+cifsayi_kontrol(i)+ucunkati(i)+besinkati(i)
                print(f"{i} sayisi {durum}")
            break

        else:
            print("son sayi ilk sayidan buyuk olmali")



#programa aciklamalar yaparak basliyoruz
print("""

Belli bir sayi araligindaki butun tam sayilarin:
#tek,cift,
#3 e bolunur,
#5 e bolunur 
    olma durumlarini inceleyelim""")
print('''

Bunun icin sayi araliginin:
--baslangic 
--bitis noktalarini 
 belirlemelisin''')
sayikontrol()


