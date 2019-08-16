def tekfonk (a) :
    if a%2==1:
        yazı=" tek sayı"
        return yazı
    else:
        return " "
def çiftfonk(a):
    if a%2==0:
        return "çift sayı"
    else:
        return " "
def üçfonk(a):
    if a%3==0:
        return " 3 ün katı"
    else:
        return " "
def beşfonk(a):
    if a%5==0:
        return " 5 in katı"
    else:
        return " "

def sayıceşit(a,b):
    for i in range(a,b+1):
        print(i,end=" ")
        print(tekfonk(i),end=" ")
        print(çiftfonk(i),end=" ")
        print(üçfonk(i),end=" ")
        print(beşfonk(i))       
    return
                 
sayı1=int(input("Birinci sayıyı giriniz.."))
sayı2=int(input("İkinci sayıyı giriniz..."))
sayıceşit(sayı1,sayı2)


    


        
    
