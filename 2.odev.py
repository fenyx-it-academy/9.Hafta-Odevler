from functools import reduce
print(reduce(lambda x,y:x+y,list(map(lambda x: x*2,list(filter(lambda x:x%2==1, range(1,11)))))))