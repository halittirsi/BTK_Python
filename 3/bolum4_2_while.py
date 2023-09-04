sayac = 0
toplam = 0
sayi_adedi = 10
while sayac < sayi_adedi :
    girilensayi = int(input(f"{sayac+1}. sayıyı girin: "))
    toplam += girilensayi
    sayac += 1
ortalama = toplam/sayi_adedi

print(f"Girilen sayıların toplamı: {toplam}")
print(f"Girilen sayıların ortalaması: {ortalama}")