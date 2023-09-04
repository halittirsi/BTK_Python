dosya = open("deneme.txt", "r")
metin = dosya.read()
print(len(metin))

dosya = open("deneme.txt", "r")
print(dosya.read(10))

dosya = open("deneme.txt", "r")
print(dosya.readline())