class Calisan:
    sirket = "BTK"

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.f_eposta()

    def f_eposta(self):                             # e-postayı bir fonksiyon olarak aşağıda tanımladık ve bu şekilde güncelledik
        return self.ad + self.soyad + "@sirket.com"

    @classmethod
    def pi(cls):                                    #cls------ class'a ait bir özellik tanımlamak istiyorsak cls kullanıyoruz.
        return 3.14

print(Calisan.sirket)

calisan1 = Calisan("Enes", "Meselik", 50000)

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

print(calisan1.eposta)
print(calisan1.pi())
print(Calisan.pi())
