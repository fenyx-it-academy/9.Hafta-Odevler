# 9.Hafta-Odevler
ODEV 1:
Asagida ozellikleri belirtilen 4 fonksiyon belirtiniz.
1. Tek sayi kontrolu yapan fonksiyon,
2. Cift sayi kontrolu yapan fonksiyon,
3. 3’e bolunme kontrolu yapan fonksiyon,
4. 5’e bolunme kontrolu yapan fonksiyon.

Bunlardan ayri 5. bir fonksiyon yazin ve bu ilksayi ve sonsayi seklinde iki parametre alsin.

Yukarida olusturdugunuz ilk 4 fonksiyonu son olusturdugunuz fonksiyonun icinde calistirarak islemler yapiniz.
Fonksiyon verdiginiz baslangic ve bitis sayilarina gore bir liste olusturmali ve listenin icindeki sayilari
tek - cift - 3'un kati - 5'in kati durumlarina gore kontrol etmeli. Uygun durumlarda ilgili fonksiyonu cagirip o 
duruma iliskin bir cikti vermeli. 

	Orn: def sayikontrol(ilksayi,sonsayi)

	sayikontrol(1,10)
	Ornek cikti:
	1 tek sayidir
	2 cift sayidir
	3 tek sayidir
	3 ucun katidir
	4 cift sayidir
	5 tek sayidir
	5 besin katidir
	6 cift sayidir
	6 ucun katidir
	7 tek sayidir
	8 cift sayidir
	9 tek sayidir
	9 ucun katidir

ODEV 2:
Verilen bir sayi listesinin elemanlarindan tek olanlari ikiyle carpan ve hepsini toplayip sonucu veren bir fonksiyon yaziniz. Map, filter ve reduce kullaniniz.

ODEV 3:
pzt = [
  {
    isim: 'Fonksiyonlara calis',
    sure: 180,
  },
  {
    isim: 'ornek coz',
    sure: 120,
  },
  {
    isim: 'odev kontrol',
    sure: 20,
  },
  {
    isim: 'bayramlasma',
    sure: 200,
  },
]

sali = [
  {
    isim: 'gelecek haftaya hazirlik',
    sure: 240,
  },
  {
    isim: 'ornek cozumlerine devam et',
    sure: 180,
  },
  {
    isim: 'kahve molasi',
    sure: 10,
  },
  {
    isim: 'kitap oku',
    sure: 200,
  },
  {
    isim: 'spor yap',
    sure: 40,
  },
]

Not: Sureler dakika cinsindendir!

Map, filter ve reduce kullanarak yukarida belirtilen iki gunluk plan neticesinde kac puan kazanilacagini hesaplayan bir program yaziniz. 

	•	Map ile sureleri saat cinsine donusturun.
	•	Iki saatin altindaki tum rutinleri filter ile eleyin. 
	•	Sureleri saatte 20 puan kazandiracak sekilde saatlik bazda guncelleyin. 
	•	Kusurlu degerleri .round() ile yuvarlayin. 
	•	Son olarak reduce ile kullanicinin kac puan kazandigini hesaplayin.
	•	Degisken isimlerinin duzgun ve anlasilir olmasina ozen gosterin.

