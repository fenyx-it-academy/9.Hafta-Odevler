print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

from functools import reduce

lst = [1, 2, 3, 4, 5]
print("Sum of multiply with 2 and odd numbers in the list: ",
      reduce(lambda z, t: z + t, list(map(lambda y: 2 * y, filter(lambda x: x % 2 != 0, lst)))))
