#1
not1=64
not2=86
not3=70
ortalama = (not1+ not2+ not3)/3
print(int(ortalama))

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
