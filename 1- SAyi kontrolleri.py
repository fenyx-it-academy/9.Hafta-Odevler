def teksayi(sayi):

    if sayi%2!=0:
        return sayi


def ciftsayi(sayi):

    if sayi%2==0:
        return sayi


def ucebolunme(sayi):

    if sayi%3==0:
        return sayi


def besebolunme(sayi):

    if sayi%5==0:
        return sayi

def genelislem(start,finish):

    for sayi in range(start,finish):

        if teksayi(sayi):
            yield sayi,"sayisi tek sayidir"

        if ciftsayi(sayi):
            yield sayi, "sayisi cift sayidir"

        if ucebolunme(sayi):
            yield sayi, "ucun katidir"
            
        if besebolunme(sayi):
            yield  sayi, "besin katidir"



print(*list(genelislem(1,10)),sep="\n")


