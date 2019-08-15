from functools import reduce        #reduce kullanmak icin cagirdik

def islem(ilksayi,ikincisayi):
    a=list(range(ilksayi,ikincisayi))

    print(list( map(lambda x : x*2, filter(lambda x : x%2!=0,a))))  #tek sayilari bulup ikiyle carpip yazdirdik)
    print(reduce(lambda x,y : x+y , a)) #listedeki butun sayilari topladik

islem(1,5)


# Asagidaki de sadece Aldigi tek sayilari toplayan kod


# def islem(ilksayi,ikincisayi):
#     a=list(range(ilksayi,ikincisayi))
#
#     b=list( map(lambda x : x*2, filter(lambda x : x%2!=0,a))) #degisken vermek durumunda kaldik,tek sayilari ikiyle carptik
#     c = [reduce(lambda x,y : x+y , b)]    #yukaridaki degiskeni kullanarak reduce nin ikinci ogesini koyduk, ilginctir list yapinca olmadi kendimiz liste isareti yaptik.
#     return c
# print(islem(1,5))

