# Görevleri sor, kontrol et, görevi bitir, hepsi bitince uygulamayı kapat
#bugün hangi işleri yapacaksın
#işleri yazacaksın
#yaptıklarını çıkartacaksın
#görev listesi yap
#görevleri kontrol et
#listeden sil

yapilacaklar = []
while True:
    isler = input("Bu gün neler yapacaksın: ")
    if isler != "x":
       yapilacaklar.append(isler)
    else:
        print("Yapılacaklar listeniz", yapilacaklar)
        break
for i in range(len(yapilacaklar)):
    print(input(f'{yapilacaklar[0]}, ne durumda? '))