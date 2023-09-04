"""

# part-1(For ile)
adet = int(input("Kaç adet zerzevat alacaksınız: "))
zerzevat = []
for dd in range(1,adet+1):
   urun = input(f"{dd} nolu ürünü giriniz: ")
   zerzevat.append(urun)
print("pazar listeniz", zerzevat)


"""




# part-2(While ile)
mesaj = """
Pazar listesi programına hoşgeldiniz,
programdan çıkmak için x'e basınız
"""
print(mesaj)
zerzevat = []
while True:
    urun = input("ürün giriş yapın veya X'e basınız")
    if urun.lower() !="x":
      zerzevat.append(urun)
    else:
      print("pazar listeniz", zerzevat)
      break