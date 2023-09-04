import random

sayi = random.randrange(1,100)
print(sayi)
tahminSayisi = 10
taban = 0
tavan = 101

while tahminSayisi >=1:
    tahmin = int(input(f'{taban} - {tavan} arasında bir sayı girin: '))
    if tahmin == sayi:
        print("Tebrikler")
        break
    elif tahmin > sayi:
        tavan = tahmin
    elif tahmin < sayi:
        taban = tahmin
    tahminSayisi -= 1
    print("Kalan hakkınız:", tahminSayisi)

