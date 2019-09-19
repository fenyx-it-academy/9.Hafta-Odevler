# Verilen bir sayi listesinin elemanlarindan
# tek olanlari ikiyle carpan ve hepsini toplayip sonucu veren bir fonksiyon yaziniz.
# Map, filter ve reduce kullaniniz.

from functools import reduce

nums = [5, 6, 9, 12, 17, 101]


def operation(*args):
    liste_op = list(map(lambda a: a * 2, filter(lambda a: a % 2 != 0, *args)))
    print(f"The operation list: {nums},\nDoubled odd numbers: {liste_op},"
          f"\nAnd the total is »»{reduce(lambda a, b: a + b, liste_op)}««")
operation(nums)
