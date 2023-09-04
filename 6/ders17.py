import random
import os


def oyun(dosya_adi):
    dosya = open(dosya_adi, "a")
    rastgele = random.randrange(1, 100)
    dosya.write(str(rastgele)+"+")
    tahminSayisi = 10
    taban = 0
    tavan = 100
    while tahminSayisi >= 1:
        tahmin = int(input("Bir sayı giriniz"))
        dosya.write(str(tahmin) + ",")
        if tahmin == rastgele:
            dosya.write("+kazandiniz" + "\n")
            print("Tebrikler")
            break
        elif tahmin > rastgele:
            print("daha küçük giriniz")
            tavan = tahmin
        elif tahmin < rastgele:
            print("daha büyük giriniz")
            taban = tahmin
        tahminSayisi -= 1
        print("kalan hakkınız", tahminSayisi)
        if tahmin == 0:
            dosya.write("kaybettiniz" + "\n")
            dosya.close()


def istatiktik(dosya_adi):
    dosya = open(dosya_adi, "r")
    print(dosya.readlines())
    dosya.close()


def cikis():
    print("çıkış Yapıldı")
    exit()


while True:
    dosya_adi = "oyun.txt"
    
    if not (os.path.exists(dosya_adi)):
        dosya = open(dosya_adi, "x")
        dosya.close()
    cevap = int(input("Oyun için :1 \n İstatistik için : 2\t Çıkış için: 3\t"))
    if cevap == 3:
        cikis()

    elif cevap == 1:
        oyun(dosya_adi)

    elif cevap == 2:
        istatiktik(dosya_adi)
