"""
ODEV 2: Verilen bir sayi listesinin elemanlarindan tek olanlari ikiyle carpan ve hepsini toplayip sonucu veren
bir fonksiyon yaziniz. Map, filter ve reduce kullaniniz.
"""


from functools import reduce
mylist=[1,2,3,4,4,5]
print (reduce(lambda x,y: x+y ,map( lambda x:x*2, (filter(lambda x :x%2!=0,mylist)))))
