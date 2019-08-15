print("********** Number Control **********")
def odd_number(x):
    if x%2 != 0:
        return print(x,"is a odd number")
def even_number(x):
    if x%2 == 0:
        return print(x,"is a even number")
def division_3(x):
    if x%3 == 0:
        return print(x,"is a multiple of 3")
def division_5(x):
    if x%5 == 0:
        return print(x,"is a multiple of 5")
def number_control(first,last):
    for i in range (first,last+1):
        odd_number(i)
        even_number(i)
        division_3(i)
        division_5(i)
number_control(1,10)
        
