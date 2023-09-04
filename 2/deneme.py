disiplin = input("Disiplin cezası aldınız mı? ")
if disiplin == "hayır":
    devamsizlik = int(input("Devamsızlık durumunuzu giriniz:"))
    if devamsizlik <= 5:
        notOrtalamasi = int(input("Not ortalamanizi giriniz:"))
        if notOrtalamasi >= 70 and notOrtalamasi<85 :
            print("Teşekkür Belgesi Almaya Hak Kazandınız.")
        elif notOrtalamasi >= 85:
            print("Takdir Belgesi Almaya Hak Kazandınız.")
        else:
             print("Not ortalamanız yetersiz.")
    else:
        print("Devamsızlık nedeniyle belge alamazsınız.")
else:
    print("Disiplin cezası nedeniyle belge alamazsınız.")