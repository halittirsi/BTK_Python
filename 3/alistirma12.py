carpim = 1
girilenSayi = 0
while True: #sonsuz döngü oluşturduk
    sayi = int(input("Bir sayı giriniz: "))
    girilenSayi += 1
    if girilenSayi == 10:
        print("Girdiğiniz sayıların çarpımı: ", carpim)
    if sayi == 0 :
        print("Girdiğiniz sayıların çarpımı: ", carpim)
        break
    carpim *= sayi
    