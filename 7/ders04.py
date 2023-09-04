class Ogrenci:
    bolum = "Mühendislik"
    def __init__(self):     #constructer, bir class tanımlandığında çalışmaya başlayan komut
        self.ad = 'Halit'
        self.soyad = ''

ogr1 = Ogrenci()
print(ogr1.ad)
print(ogr1.bolum)
print(Ogrenci.bolum)
#Ogrenci.ad yapamayız çünkü ad, self olarak tanımlandı.