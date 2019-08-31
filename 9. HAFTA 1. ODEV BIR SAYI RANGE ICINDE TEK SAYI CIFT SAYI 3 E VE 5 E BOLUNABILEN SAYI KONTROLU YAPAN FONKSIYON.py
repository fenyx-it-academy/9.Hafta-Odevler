##### Tek sayi kontrolu #####
print ("Lutfen ilki kucuk olmak uzere 2 adet sayi degeri giriniz")
def tek(a):
    if a%2 != 0:
        return a,"odd number."

#### Cift sayi kontrolu ####
def cift(a):
    if a%2 == 0:
        return a,"even number."

## Uce Bolunme ##
def ucebol(a):
    if a%3 == 0:
        return a,"divisible with 3."

# 5e bolunme #
def besebol(a):
    if a%5 == 0:
        return a,"divisible with 5."
new=[tek,cift,ucebol,besebol]

def check(sayi):  #burada yukaridaki fonksiyonlari cagiran baska bir fonksiyon yaziyoruz.
    start=int(input("Firstvalue:"))
    end= int(input("Lastvalue:"))
    liste = list(range(start,end))
    for i in liste:
        value=list(map(lambda x:x(i),new))
        nvalue=list(filter(lambda x:x!=None,value))
        for i in nvalue:
            for j in i:
                print(j,sep=" ")

check(2)
