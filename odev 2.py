from functools import reduce
sayi = [5,6,9,12,8,68,35,21,45,256]

def islem(*args):
    liste_islem = list(map(lambda a: a*2, filter(lambda a: a%2!=0, *args)))
    print(f"islem yapilacak liste : {sayi}")
    print(f"tek sayilarin iki kati alinan liste : {liste_islem}")

    print(f"islem yapilan listenin toplami : {reduce(lambda a,b: a+b , liste_islem)}")

islem(sayi)