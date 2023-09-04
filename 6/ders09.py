# * işareti n tane parametre gelecek olduğunu belirtiyor. sayilar ise list tipinde veri oluşturur.
def sayiyazdir(*sayilar): 
    x = [*sayilar]
    print(x)
    print(*sayilar)
    for sayi in x:
        print(sayi)

sayiyazdir(1,2,3,4,5,6)
