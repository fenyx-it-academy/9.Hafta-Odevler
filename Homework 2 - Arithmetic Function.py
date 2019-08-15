from functools import reduce
print("********** Arithmetic Function **********")
n=[i for i in range(1,11)]
#The explanation is not clear enough.
#If only the odd numbers are multiplied by two and the results are summed, the following function is appropriate.

print(reduce(lambda x,y:x+y,map(lambda x:x*2,filter(lambda x: x if x%2==1 else False,n))))

      
#The explanation is not clear enough.
#If the odd numbers are multiplied by two and the entire list (the results of odd numbers multiplied by two and the even numbers of the list) is added, the following function is appropriate.
def arithmetic(args):
    x=reduce(lambda x,y:x+y,map(lambda x:x*2,filter(lambda x: x if x%2==1 else False,n)))
    y=reduce(lambda x,y:x+y,filter(lambda x: x if x%2!=1 else False,n))
    return x+y
print(*set(map(arithmetic,n)))

#Another Method

def odd_number(args):
    return(reduce(lambda x,y:x+y,map(lambda x:x*2,filter(lambda x: x if x%2==1 else False,n))))
def even_number(args):
    return(reduce(lambda x,y:x+y,filter(lambda x: x if x%2!=1 else False,n)))
def arithmetic(args):
    return odd_number(args)+even_number(args)
print("With another method:",*set(map(arithmetic,n)))
