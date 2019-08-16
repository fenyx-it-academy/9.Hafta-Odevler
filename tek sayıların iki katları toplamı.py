from functools import reduce
#reduce import edilir
liste=[1,2,3,4,5,6,7,8,9,10]
#liste tanımlama
print(reduce(lambda x,y: x+y,(map(lambda x: 2*x,filter(lambda x: x%2==1,liste)))))
# filter(lambda x: x%2==1,liste) listeden aldığı elemanların tek olanları ile kaynak liste olusturur
#(map(lambda x: 2*x,filter(lambda x: x%2==1,liste)) olusturulan tek elemanlar listesinin elemanlarını-
# iki ile carparak kaynak liste olusturur
#(reduce(lambda x,y: x+y,(map(lambda x: 2*x,filter(lambda x: x%2==1,liste))))) en son olusturulan-
# kaynak listenin elemanlarını toplar ve tek deger dondurur



