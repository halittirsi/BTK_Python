sayilar = []

for dd in range(10):
    sayilar.append(int(input(f'{dd+1}. sayıyı giriniz')))

eb = sayilar[0]         # ilk girilen sayıyı hem en küçük hem en büyük olarak girdik sayı geldikce büyük ve küçük değişecek.
ek = sayilar[0]
for sayi in sayilar:            
    if eb < sayi:
        eb = sayi
    if ek > sayi:
        ek = sayi
print("En büyük sayı: ", eb)
print("En küçük sayı: ", ek)