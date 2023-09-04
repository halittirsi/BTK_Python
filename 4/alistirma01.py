# list yöntemi örneği
ad = input("Adınızı girin: ")
soyad = input("Soyadınızı girin: ")
yas = int(input("Yaşınızı girin: "))
boy = float(input("Boyunuzu girin: "))
cinsiyet = bool(input("Cinsiyetinizi girin: E:1 K:0 "))
ogrenci = [ad, soyad, yas, boy, cinsiyet]

for dd in ogrenci:
    print(dd)