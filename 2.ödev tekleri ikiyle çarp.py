from functools import reduce

def sayılar(sayı,sayı1):
    a=list(range(sayı,sayı1))

    print(list( map(lambda x : x*2, filter(lambda x : x%2!=0,a))))  #tek sayılar ikiyle çarptık)
    print(reduce(lambda x,y : x+y , a)) #listedeki sayıları topladık
sayı =int(input("bir sayı giriniz:"))
sayı1 =int(input("bir sayı giriniz:"))
sayılar(sayı,sayı1)
