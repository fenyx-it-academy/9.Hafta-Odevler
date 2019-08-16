def tek(sayı):
    #tek sayı fonksiyon ve parametre tanımlma
    if sayı%2==1:
        #iki ile bolumunden kalan 1 ise return yap
        return (f'{sayı} tek sayıdır.')

def cift(sayı):
    #cift sayı fonksiyonu ve parametre tanımlama
    if sayı%2==0:
        #iki ile bolumunden kalan 0 ise return yap
        return (f'{sayı} çift sayıdır.')

def uc_bol(sayı):
    #uc bolunebilme fonksiyonu ve parametre tanımlama
    if sayı%3==0:
        #uce bolumunden kalan 0 ise return yap
        return (f'{sayı} üçün katıdır.')

def bes_bol(sayı):
    #bes ile bolunebilme foksiyonu ve parametre tanımlama
    if sayı%5==0:
        #bes ile bolumunden kalan 0 ise return yap
        return (f'{sayı} beşin katıdır.')

def sayı_kontrol(ilk,son):
    #fonksiyon ve iki parametre tanımlama
    for i in range(ilk,son+1):
        #fonksiyon parametreleri arası degerler icin dongu
        if tek(i)!=None:
            #tek fonksiyon degeri none degilse
            print (tek(i))
            #tek fonksiyon sonucunu printle
        if cift(i)!=None:
            #çift fonksiyon degeri none degilse
            print (cift(i))
            #çift fonksiyon sonucunu printle
        if uc_bol(i)!=None:
            #uc_bol fonksiyon degeri none degilse
            print (uc_bol(i))
            #uc_bol fonksiyon sonucunu printle
        if bes_bol(i)!=None:
            # bes_bol fonksiyon degeri none degilse
            print (bes_bol(i))
            # bes_bol fonksiyonu sonucunu printle

sayı_kontrol(31,130)

