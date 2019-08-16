from functools import reduce

def islem(sayılar):
    print(reduce(lambda a,b: a+b ,list(map(lambda y : 2*y,list(filter(lambda z: z%2==1,sayılar))))))

islem([1,4,5,7,10])
             
