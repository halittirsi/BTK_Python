class Calisan:
    sirket = "BTK"

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"

print(Calisan.sirket)

calisan1 = Calisan("Enes", "Meşelik", 50000)

print(calisan1.sirket)
print(calisan1.ad)
print(calisan1.maas)

calisan1.maas *= 1.5            #Maaş değiştirdik
print(calisan1.maas)

calisan1.sirket = "Aselsan"     #Enesin çalıştığı şirketi değiştirdik 
print(calisan1.sirket)          #Şirket bilgisini gösterdik
print(Calisan.sirket)           # class'ın şirket bilgisi ile enesin şirket bilgisinin değişmediğini gösterdik.

Calisan.sirket = "THY"          # BTK'yı değiştirdik, THY yaptık çalışanların şirketleri THY olarak değişti ama enesin şirketi en son
print(Calisan.sirket)           # Aselsan olduğu için onun işi değişmez hala Aselsandır.
print(calisan1.sirket)

calisan2 = Calisan("Gülce", "GOK", 50000.5)     #Gülceyi çalışan olarak tanımladık ve şirketini yazdırdık.
print(calisan2.sirket)                          # THY olduğunu görebiliriz.




