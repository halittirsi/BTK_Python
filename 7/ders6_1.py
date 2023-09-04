class Calisan:
    per_sayisi = 0
    zam_oranı = 1.1

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
        Calisan.per_sayisi = Calisan.per_sayisi + 1

    def tamad(self):
        return "adı : {}  soyadı : {}".format(self.ad,self.soyad)
    
    def arttir(self):
        # self.maas = (self.maas*1.05)
        # self.maas = (self.maas * Calisan.zam_oranı)
        self.maas = (self.maas * self.zam_oranı)

#Personel sayısına müdahele ediyoruz
print(Calisan.per_sayisi)
personel1 = Calisan("Ali", "Demir", 2500)
print(Calisan.per_sayisi)
personel2 = Calisan("Kerim", "Bakır", 2000)
print(Calisan.per_sayisi)

#Maaş Arttırıyoruz
print(personel1.maas)
personel1.arttir()
print(personel1.maas)

# Personel2'ye %15 zam yapıyoruz
print(personel2.maas)
personel2.zam_oranı = 1.15
personel2.arttir()
print(personel2.maas)