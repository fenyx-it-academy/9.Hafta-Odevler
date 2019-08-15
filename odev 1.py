def teksayi(a):         # Tek sayilari kontrol eden fonksiyon
    if a%2!=0:
        return True
    return False

def ciftsayi(a):        # cift sayilari kontrol eden fonksiyon
    if a%2==0:
        return True
    return False

def ucebol(a):          # uce bolunebilen sayilari kontrol eden fonksiyon
    if a%3==0:
        return True
    return False

def besbol(a):          # bese bolunebilen sayilari kontrol eden fonksiyon
    if a%5==0:
        return True
    return False

def kontrol(ilksayi, sonsayi):  #iki arguman arasindaki sayilari tek, cift , 3. kati ve 5. kati olma durumuna gore kontrol eden fonksiyon
    for i in range(ilksayi, sonsayi):
        if teksayi(i):
            print(f"{i} tek sayidir.")
        if ciftsayi(i):
            print(f"{i} cift sayidir.")
        if ucebol(i):
            print(f"{i} ucun katidir.")
        if besbol(i):
            print(f"{i} besin katidir.")

cikis=1
while cikis==1:                 # iki sayi girisi alan dongu. bu sayilar arasindaki tum sayilari kontrol fonksiyonu ile tariyoruz
    ilksayi = int(input("Lutfen araligin alt sinirini giriniz :"))
    sonsayi = int(input("Lutfen araligin ust sinirini giriniz :"))

    kontrol(ilksayi,sonsayi)


    cikis = int(input("Cikis icin '0' / Devam etmek icin '1' i tuslayiniz :"))

