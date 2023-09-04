# dictionary(sözlük)
# sıralı ve değişme özelliği vardır.
# {key: Value, }

tureng = {"araba":"car","kırmızı":"red","mavi":"blue"}
print(tureng)
print(type(tureng))
print(tureng.get("araba"))
print(tureng["araba"])
print(tureng.keys())
print(tureng.values())
print(tureng.items())
ikililer = tureng.items()
print(type(ikililer))
for dd in tureng:   
    print(dd)                       #1. yani keyleri yazdırdı.
    print(tureng.get(dd))           #2. yani value ları yazdırdı
    print(tureng[dd])
    print(