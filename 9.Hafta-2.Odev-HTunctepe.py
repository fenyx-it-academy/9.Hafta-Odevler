from functools import reduce


def mathFunction(myList):
    return reduce(lambda num1, num2:num1+num2,
                  (list(map(lambda num:num*2,
                            (list(filter(lambda num: (num % 2 == 1), myList)))))))


myList = [1, 2, 3, 4, 5, 7, 8, 9, 10]
print(mathFunction(myList))