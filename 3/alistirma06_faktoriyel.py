baslangic = int(input("Başlangıç değerini giriniz "))
bitis = int(input("Bitiş değerini giriniz "))
artis = int(input("Artış değerini giriniz "))
faktoriyel = 1
for dd in range(baslangic,bitis, artis):
    faktoriyel *= dd
    print(dd,faktoriyel)