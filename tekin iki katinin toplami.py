print("""

Bu kod ile istediginiz listesinin icindeki elemanlardan
#sayi olanlari bulup
#tek olanlari bulup
#iki katini alip
#sonuclarin toplamini bulacagiz

""")


def liste():
    grup = []
    while True:
        print("listenize eklemek istediginiz elemanlari giriniz(bitirmek icin OK yazin):")
        a=input("")
        if a=="OK":
            break
        else:
            grup.append(a)
    print(grup)
    return grup



from functools import reduce

fonksiyon=print(reduce(lambda x,y:x+y,map(lambda x:x*2,filter(lambda x:x%2==1,map(lambda x:int(x),filter(lambda x:x.isdigit(),liste()))))))






