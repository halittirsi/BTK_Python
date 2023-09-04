devamsizlik = int(input("Kaç gün devamsızlık yaptınız "))
if devamsizlik<10:

    not1 = int(input("birinci not "))
    not2 = int(input("ikinci not "))
    not3 = int(input("üçüncü not "))


    if (not1+not2+not3)/3 >= 50:
        print("dersi geçtin")
    else:
        print("dersten kaldın")
else:
    print("devamsızlıktan kaldınız")