birinciSayi = input("ilk sayı giriniz")
ikinciSayi = input("ikinci sayıyı giriniz")
ucuncuSayi = input("Üçüncü sayıyı giriniz")
if birinciSayi > ikinciSayi and birinciSayi > ucuncuSayi and ikinciSayi>ucuncuSayi:
    print( birinciSayi, ikinciSayi, ucuncuSayi)
elif birinciSayi > ikinciSayi and birinciSayi > ucuncuSayi and ikinciSayi<ucuncuSayi:
    print(birinciSayi,ucuncuSayi,ikinciSayi)
elif ikinciSayi>birinciSayi and ikinciSayi>ucuncuSayi and birinciSayi<ucuncuSayi:
    print(ikinciSayi,birinciSayi,ucuncuSayi)
elif ikinciSayi>birinciSayi and ikinciSayi>ucuncuSayi and ucuncuSayi>birinciSayi:
    print(ikinciSayi,ucuncuSayi,birinciSayi)
elif ucuncuSayi>birinciSayi and ucuncuSayi>ikinciSayi and birinciSayi>ikinciSayi:
    print(ucuncuSayi,birinciSayi,ikinciSayi)
elif ucuncuSayi>birinciSayi and ucuncuSayi>ikinciSayi and ikinciSayi>birinciSayi:
    print(ucuncuSayi,ikinciSayi,birinciSayi)
    