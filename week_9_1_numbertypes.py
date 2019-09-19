def check(first, last):
    def odd_number(i):
        if i % 2 != 0:
            return print(i, "..is an odd number", sep="")

    def even_number(i):
        if i % 2 == 0:
            return print(i, "..is an even number", sep="")

    def divide_3(i):
        if i % 3 == 0:
            return print(i, "..is divisible to 3", sep="")

    def divide_5(i):
        if i % 5 == 0:
            return print(i, "..is divisible to 5", sep="")

    for i in range(first, last):
        if odd_number(i):
            print(i, "..is an odd number ", sep="")
        if even_number(i):
            print(i, "..is an even number", sep="")
        if divide_3(i):
            print(i, "..is divisible to 3", sep="")
        if divide_5(i):
            print(i, "..is divisible to 5", sep="")


while True:
    first = int(input('Please enter your first number exit> 0 : '))
    last = int(input("Please enter your second number exit> 0: "))
    if first == 0:
        print("Exiting!Bye")
        break
    if last == 0:
        print("Exiting!Bye")
        break
    else:
        check(first, last)
