#1
not1=64
not2=86
not3=70
ortalama = (not1+ not2+ not3)/3
print(int(ortalama))

print("İlk notunuzu giriniz")
ilk = int(input())

print("İkinci notunuzu giriniz")
ikinci = int(input())

print("Üçüncü notunuzu giriniz")
ucuncu = int(input())

ortalama_not = (ilk+ ikinci+ ucuncu)/3
print(int(ortalama_not))


#2
print("Adınız nedir?")
ad=str(input())             #input ile alınan her veri string olur.
print("Kaç yaşındasınız?")
yas=int(input())
print(ad*yas)

#3
print("Pi kaç olsun?")
pi=float(input())
print("Yarıçap kaç olsun?")
yaricap=float(input())
cevre = 2*pi*yaricap
alan = pi*yaricap**2
print(cevre)
print(alan)

#4
print("Lütfen doğum tarihinizi giriniz")
dogum_tarihi=int(input())
uygunluk = 2023 - dogum_tarihi >= 18
print(uygunluk)

#5
print("Faiz oranı nedir?")
faiz_orani = float(input())
print("Ana paranızın miktarını giriniz")
ana_para = float(input())
yillik_faiz = (faiz_orani*ana_para)/100
print("Yıllık faiz oranı:",float(yillik_faiz))

#6
print("Boyunuz kaç m?")
boy = float(input())
print("Kilonuz kaç kg?")
kilo = float(input())
kitle_endeksi = float(kilo/boy**2)
print(kitle_endeksi)

#7
print("İlk kişinin adı nedir?")
isim1 = input()
print("İkinci kişinin adı nedir?")
isim2 = input()
adaslık = isim1 == isim2
print(adaslık)

#8
print("Yıl sonu not ortalamanızı giriniz")
notOrtalamasi = int(input())
basariDurumu = notOrtalamasi>=70
print(basariDurumu)

#9
print("Aldığınız mesafe kaç m")
alinanYol = int(input())
print("Geçiş süreniz nedir?")
gecenZaman = int(input())

ceza = alinanYol/gecenZaman > 130
print(ceza)


#10
print("Kaç gün çalıştınız?")
gun = int(input())
tutar = gun*375
print(tutar)
