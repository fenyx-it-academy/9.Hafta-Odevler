print('b.')
'''
ODEV 2: Verilen bir sayi listesinin elemanlarindan tek olanlari ikiyle carpan ve 
hepsini toplayip sonucu veren bir fonksiyon yaziniz. Map, filter ve reduce kullaniniz.
'''
from functools import reduce

liste=[1,2,3,4,5,7,8,9,10]

print('sonuc :',reduce(lambda a,b:a+b,list(map(lambda x:x*2,list(filter(lambda x:x%2==1,liste))))))


