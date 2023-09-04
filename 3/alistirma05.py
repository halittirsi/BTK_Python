toplam = 0
baslangic = int(input("Başlangıç değerini giriniz "))
bitis = int(input("Bitiş değerini giriniz "))
artis = int(input("Artış değerini giriniz "))

for i in range(baslangic, bitis, artis):
    toplam += i
    print(i, toplam)
