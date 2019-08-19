from functools import reduce
sayi=range(1,100)
sonuc=reduce(lambda sayi1,sayi2:sayi1+sayi2,list(map(lambda sayi:sayi*2,list(filter(lambda sayi:sayi%2 != 0,sayi)))))
            # Filter ile tek sayilar filtrelendi
            # Map ile sayilar 2 ile carpildi
            # Reduce ile listedeki tum degerler toplandi
print("Listedeki tek sayilarin iki ile carpilip toplanmis hali: ", sonuc)