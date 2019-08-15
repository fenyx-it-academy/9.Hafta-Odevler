print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


def findi(first, last):

    def odd(number):
        if number % 2 == 1:
            return number
        else:
            return False

    def even(number):
        if number % 2 == 0:
            return number
        else:
            return False

    def triple(number):
        if number % 3 == 0:
            return number
        else:
            return False

    def quintet(number):
        if number % 5 == 0:
            return number
        else:
            return False

    for i in range(first, last):
        if odd(i):
            print(f"{i} is odd number.")
        if even(i):
            print(f"{i} is even number.")
        if triple(i):
            print(f"{i} is 3 times number.")
        if quintet(i):
            print(f"{i} is 5 times number.")


first = int(input("ilk sayi: "))
last = int(input("ikinci sayi: "))
findi(first, last)