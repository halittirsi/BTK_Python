class Ogrenci: # Class olarak öğrenci tanımladık.
    ad = ''     # ad özelliğinin stribg olduğunu belirttik
    def selamla(self):  #fonksiyon, selamlama fonksiyonu oluşturduk ve aşağıda bunu çağırarak kullandık.
        print("Merhaba")

ogr1 = Ogrenci()
ogr1.ad = "Halit"
print(ogr1.ad)
ogr1.selamla()

ogr2 = Ogrenci()
ogr2.ad = "Semih"
print(ogr2.ad)