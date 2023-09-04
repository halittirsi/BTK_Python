sayi = int(10)
for sayimiz in range (1,100):
    sayimiz = int(input("1 ile 100 arasında bir sayı giriniz: "))
    if sayimiz == 10:
        print("doğru tahmin")
        
    elif sayimiz>10:
        print("daha küçük tahmin dene")
    elif sayimiz<10:
        print("daha büyük tahmin dene")
    
