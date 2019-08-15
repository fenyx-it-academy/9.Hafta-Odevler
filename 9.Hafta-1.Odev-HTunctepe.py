def isOddNumber(num):
    if num % 2 == 1:
        return print(num, 'is an odd number.')


def isEvenNumber(num):
    if num % 2 == 0:
        return print(num, 'is an even number.')

def isMultipleOf3(num):
    if num % 3 == 0:
        return print(num, 'is multiple of 3.')

def isMultipleOf5(num):
    if num % 5 == 0:
        return print(num, 'is multiple of 5.')

def executer(firstNum, lastNum):
    for num in range(firstNum, lastNum+1):
        isOddNumber(num)
        isEvenNumber(num)
        isMultipleOf3(num)
        isMultipleOf5(num)

# To execute the program within a range, uncomment line 28 and
# replace x and y with the desired numbers.

# executer(x, y)