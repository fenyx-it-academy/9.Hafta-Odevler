odd_number=list(filter(lambda x:x%2==1, range(1,10)))
even_number=list(filter(lambda x:x%2==0, range(1,10)))
multiples_three=list(filter(lambda x:x%3==0, range(1,10)))
multiples_five=list(filter(lambda x:x%5==0, range (1,10)))


def control (first,last):
    def odd_number (i):
        if i % 2 != 0:
            return print(i, "It is an odd number" )

    def even_number(i):
        if i % 2 == 0:
            return print(i, "It is an even number")

    def multiples_three(i):
        if i % 3 == 0:
            return print(i, "It is multiple to three")

    def multiples_five(i):
        if i % 5 == 0:
            return print(i, "It is multiple to five")


    for i in range(first, last):
        if odd_number(i):
            print(i, " is an odd number ")
        if even_number(i):
            print(i, "is an even number")
        if multiples_three(i):
            print(i, "is multiple to three")
        if multiples_five(i):
            print(i, "is multiple to five")

first = int(input("first number: "))
last = int(input("second number: "))
control(first, last)