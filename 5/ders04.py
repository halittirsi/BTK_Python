import random

rastgele = random.randrange(1,100)
print(rastgele)

tahminSayisi = 10
taban = 0
tavan = 101
while tahminSayisi >=1:
    tahmin = random.randrange(taban,tavan)
    print(tahmin)
    if tahmin == rastgele:
        print("Tebrikler")
        break
    elif tahmin > rastgele:
        tavan = tahmin
    elif tahmin < rastgele:
        tabana = tahmin
    tahminSayisi -= 1
    print("Kalan hakkınız", tahminSayisi)