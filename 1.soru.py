teksayi=lambda sayi:sayi%2!=0
ciftsayi=lambda sayi:sayi%2==0
uc= lambda sayi:sayi%3==0
bes=lambda sayi:sayi%5==0

def sayikontrol(sayi):
  if bes(sayi):
    print(sayi, "besin katidir.")
  if uc(sayi):
    print(sayi,"ucun katidir. " )
  if ciftsayi(sayi):
    print(sayi," cift sayidir. ")
  if teksayi(sayi):
    print(sayi," tek sayidir. ")

sayi1 = input("Birinci sayi araligini giriniz: ")
sayi2 = input("Ikinci sayi araligini giriniz: ")
list(map(sayikontrol,range(int(sayi1),int(sayi2))))
