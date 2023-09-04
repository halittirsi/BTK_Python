#turnuva deneyimi
boy = int(input("Boy bilginizi giriniz: "))

if boy >= 180:
    okul = input("Üniversite öğrencisi misin? ")

    if okul == "evet" :
        print("Turnuvaya katılabilirsiniz")
    else:
        print("Turnuvaya katılamazsınız")
else:
    print("Boyunuz uygun değil")