################################ ODEV 1:

print("""There is a function blah blah, enter the first and the second number
        you want to evaluate their range in. """)
a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))

def odd(x):
    if x % 2 != 0:
        print(x, "is an odd number.")

def even(x):
    if x % 2 == 0:
        print(x, "is an even number.")

def multipleof3(x):
    if x % 3 == 0:
        print(x, "is a multiple of 3.")

def multipleof5(x):
    if x % 5 == 0:
        print(x, "is a multiple of 5.")


#asagidaki 5 satiri belirtildigi gibi lambda ve map kullanarak yapmaya calsitim ama olmuyor, bu sekidle de duzgun calisiyor zaten.


def control(x, y) :
    for i in range(x, y):
        odd(i)
        even(i)
        multipleof3(i)
        multipleof5(i)


control(a, b)


#soyle denedim: ama yapamadim
#print(list(map(lambda x: odd, range(a, b))))
# print(list(map(lambda x: even, range(a, b))))
# print(list(map(lambda x: multipleof3, range(a, b))))
# print(list(map(lambda x: multipleof5, range(a, b))))

############################## ODEV 2

from functools import reduce

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(reduce(lambda a,b: a+b,(map(lambda x: x*2 , filter(lambda x: x%2 != 0, a)))))


################################### ODEV3:
pzt = [{'isim': 'Fonksiyonlara calis', 'sure': 180, },
       {'isim': 'ornek coz', 'sure': 120, },
       {'isim': 'odev kontrol', 'sure': 20, },
       {'isim': 'bayramlasma', 'sure': 200, }]

sali = [{'isim': 'gelecek haftaya hazirlik', 'sure': 240, },
        {'isim': 'ornek cozumlerine devam et', 'sure': 180, },
        {'isim': 'kahve molasi', 'sure': 10, },
        {'isim': 'kitap oku', 'sure': 200, },
        {'isim': 'spor yap', 'sure': 40, }]


from functools import reduce


twodays = pzt + sali

a=reduce(lambda sayi1,sayi2:sayi1+sayi2,list(filter(lambda sayi:sayi>2,list(map(lambda sozluk:round(sozluk["sure"]/60),twodays)))))
print(a*20)













