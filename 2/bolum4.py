sayi_adedi = 20
sayac = 0
tek_sayi_adedi = 0
tek_sayi_toplami = 0
cift_sayi_adedi = 0
cift_sayi_toplami = 0

while sayac < sayi_adedi:
    sayi = int(input(f"{sayac+1}. sayıyı giriniz:  "))
    sayac += 1
    if sayi % 2 == 1:
        tek_sayi_toplami += sayi
        tek_sayi_adedi += 1
    else:
        cift_sayi_adedi += 1
        cift_sayi_toplami += sayi

print(tek_sayi_toplami/tek_sayi_adedi)
print(cift_sayi_toplami/cift_sayi_adedi)
