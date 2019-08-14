from functools import reduce

sayi=[1,2,3,4,5,6,7,8,9]

islem = reduce (lambda x,y:x+y,list(map(lambda x: x * 2, filter(lambda x: x % 2 != 0, sayi))))

print(islem)

