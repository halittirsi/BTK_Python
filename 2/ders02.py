print("Doğum yılınızı giriniz")
yil = int(input())
yas = 2023 - yil


"""
if yas<18:
    print("Ehliyet alamazsınız")
else:
    print("Ehliyet alabilirsin")

"""

    if not (yas <= 18):
        print("ehliyet alabilirsin")
    else:
        print("Ehliyet alamazsın")