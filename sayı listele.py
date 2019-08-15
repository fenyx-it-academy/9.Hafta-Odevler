#odev 1 hafta 9#
#sayilari listeliyoruz uygun kosullara gore#

def tek(sayi):
    if sayi%2==1:
        print(sayi," tek sayidir")
def cift(sayi):
    if sayi%2==0:
        print(sayi, " cift sayidir")
def uc(sayi):
    if sayi%3==0:
        print(sayi," uce tam bolunen sayidir")
def bes(sayi):
    if sayi%5 ==0:
        print(sayi, " bese tam bolunen sayidir")

def kontrol(a,b) :
    for i in range(a,b):                   
        tek(i)
        cift(i)
        uc(i)
        bes(i)
    print("cýkýlýyor...")
    quit()

print(kontrol(1,50))


