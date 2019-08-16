def teksayi(x):
    if x%2!=0:
        return x
def ciftsayi(x):
    if x%2==0:
        return x
def uce_bolunme(x):
    if x%3==0:
        return x
def bese_bolunme(x):
    if x%5==0:
        return x
def sayikontrol(ilk,son):
    sayilar=[]
# yukarida 4 farkli fonksiyon olsturduk ve bunlari icin bos bir liste actik
    for i in range(ilk,son):
        sayilar.append(i)
#kullanicinin verdigi sayilari range ile listemize yazdirdik ve for dongusu
#ile her sayinin hangi fonksiyonlarda isleme girecegini belirttik burda
#dongu tek seferde kirilmamasi icin return yarine yield kullandik
    for i in sayilar:
        if teksayi(i):
            yield i,'tek sayidir.'
        if ciftsayi(i):
            yield i,'cift sayidir'
        if uce_bolunme(i):
            yield i,'sayisi 3\'e bolunebilir.'
        if bese_bolunme(i):
            yield i, 'sayisi 5\'e bolunebilir.'

#fonksiyon sonucunu print ile kullaniciya verdik bu printi fonksiyonun icinde
#vermek istedik ama yapamadim
print(*list(sayikontrol(1,27)), sep='\n')


