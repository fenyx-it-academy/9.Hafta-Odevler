from functools import reduce

numbers=range (1,20)

print(reduce (lambda a,b:a+b,list(map(lambda x:x*2,list(filter(lambda x:x%2 !=0,numbers))))))
