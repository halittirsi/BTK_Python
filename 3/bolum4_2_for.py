toplam = 0
sayi_adedi = 10

for i in range(sayi_adedi):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    toplam += sayi

ortalama = toplam/sayi_adedi

print("Girilen sayıların toplamı: ", toplam)
print("Girilen sayıların ortalaması: ", ortalama)