from functools import reduce
#kutuphaneden reduce i kullanmak icin yukaridaki kodu yazdik
#ve reduce icin fonksiyon olusturduk

def liste(ilk,son):
    a=list(range(ilk,son))
    print(*list(map(lambda x: x * 2, list(filter(lambda x: x % 2 != 0,a)))),'  (2)ile carpilan tek sayilar')
    print(reduce(lambda x,y:x+y, a),' Listedeki butun sayilarin toplami')
liste(1,5)

#ikinci fonksiyonumuz ise gelen sayi araliginda bir liste olusturuyor
#ve bu fonksiyonda tek olan sayilari iki ile carpiyor ardindan
#reduce icin tanimladigimiz fonksiyonla listedeki butun sayilarim
#toplamini veriyor


#bu ikinci fonksiyonu semih beyin tavsiyesi ile range den gelen
#butun sayilari toplamak yerine sadece iki ile carptigimiz tek
#sayilarin toplamini vermis oldu
def teksayi(ilk,son):
    a=list(range(ilk,son))
    b=list(map(lambda x:x*2,list(filter(lambda x:x%2!=0,a))))
    c=[reduce(lambda x,y:x+y,b)]
    print(*c,'2 ile carpilan tek sayilar toplami')
    return
teksayi(1,5)


