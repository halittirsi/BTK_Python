ulke = input("Avrupa birliği vatandaşı mısınız")
if ulke == "evet":
    yas = int(input("Kaç yaşındasınız"))
    if yas <= 18:
        print("Turnuvaya katılabilirsiniz")
    else:
        print("yaşınız büyük")
else:
    print("sadece avrupa birliği vatandaşları katılabilir")