dosya = open("deneme.txt", "r")
for satir in dosya.readlines():
    print(satir)

dosya.close()