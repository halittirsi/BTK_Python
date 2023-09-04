#iç içe döngüler, öğrenci ortalaması hesaplayacağız

ders_sayisi = int(input("Toplam Kaç Dersiniz Var: "))
for ders in range(1,ders_sayisi+1):
    print(ders,". dersinde kaç sınavınız var: ")
    sinav_sayisi = int(input())
    for sinav in range(1, sinav_sayisi+1):
        print(ders, "dersinin", sinav, "sınav notu")

