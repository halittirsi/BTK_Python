egitim = input("Eğitim durumunuz nedir")
if egitim == "ilkokul" or egitim == "lise" or egitim == "üniversite":
    yas = int(input("Kaç yaşındasınız"))
    if yas>=18:
        print("Ehliyet alabilirsiniz")
    else:
        print("yaşınız yetersiz")
else:
    print("en az ilkokul mezunu olmak zorundasınız")