from functools import reduce
def change_list(lst):
    even_list = list(filter(lambda number: number % 2 == 0, lst))
    
    double_odd_list = list(map(lambda number: number * 2,
                 filter(lambda number: number % 2 == 1, lst)))
    
    num_list = even_list + double_odd_list
    
    result = reduce(lambda num1, num2: num1 + num2, num_list)
    return result


lst = [1,2,3,4,5,6,7]
print(change_list(lst))
