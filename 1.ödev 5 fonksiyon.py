# tek sayı ve çift sayı sorgulama
def tek_sayı(sayı):
    if int(sayı)%2==1:
        return "tek sayıdır"
    return " çift sayıdır"
sayı=input("lütfen bir sayı giriniz:")
print(tek_sayı(sayı))

# 3’e bolunme kontrolu yapan fonksiyon,
def üçeböl(sayı):
    if int(sayı)%3==0:
        return " 3'e bölünebiliyor"
    return "3'e bölünemez"

sayı=input("bir sayı giriniz:")
print(üçeböl(sayı))

#5’e bolunme kontrolu yapan fonksiyon.

def beşeböl(sayı):
    if int(sayı)%5==0:                  
        return " 5'e tam bölünür"
    return "5'e bölünemez"

sayı =input("bir sayı giriniz:")
print(beşeböl(sayı))

# 5 fonksiyonun karışımı

def karışım(sayı,sonsayı):
    
    for i in range(sayı,sonsayı):
        print(f"{i}",tek_sayı(i),üçeböl(i),beşeböl(i))

    return " "

sayı =int(input("bir sayı giriniz:"))
sonsayı =int(input("bir sayı giriniz:"))
print(karışım(sayı,sonsayı))
    
