def odd_number(number):
    if number % 2 == 1:
        print(number,"is odd number")
def even_number(number):
    if number % 2 == 0:
        print(number,"is even number")
def triple_number(number):
    if number % 3 == 0:
        print(number,"is triple number")
def quintet_number(number):
    if number % 5 == 0:
        print(number,"is quintet number")

    
def apply(firstnum ,lastnum):

    if firstnum == lastnum + 1:
        return lastnum + 1
    
    odd_number(firstnum)
    even_number(firstnum)
    triple_number(firstnum)
    quintet_number(firstnum)

    


    return firstnum + apply(firstnum + 1,lastnum)
    

        
apply(1,20)


##odd_number = lambda number: number % 2 == 1
##even_number = lambda number: number % 2 == 0
##triple_number = lambda number: number % 3 == 0
##quintet_number = lambda number: number % 5 == 0
##
##
##def apply(firstnum, lastnum):
##    if firstnum <= lastnum:
##        if odd_number(firstnum):
##            print(f"{firstnum} is odd num")
##        if even_number(firstnum):
##            print(f"{firstnum} is even num")
##        if triple_number(firstnum):
##            print(f"{firstnum} is triple num")
##        if quintet_number(firstnum):
##            print(f"{firstnum} is quintet num")
##        return apply(firstnum + 1, lastnum)
##
##
##apply(1, 20)

