# Yöntem 1
# birbirinden farklı 10 sayı girene kadar program döner.
sayilar = set()
while len(sayilar)<10:
    sayilar.add(int(input("Bir sayı giriniz: ")))
print(sayilar)

# Yöntem 2
sayi = int(input("Bir sayı giriniz: "))
eb = sayi
ek = sayisayilar = {sayi}
while len(sayilar)<10:
    sayilar.add(int(input("Bir sayı giriniz")))
for ksayi in sayilar:
    if eb < ksayi:
        eb = ksayi
    if ek > ksayi:
        ek = ksayi
    sayilar.remove(ksayi)
print("En büyük", eb)
print("En küçük", ek)
