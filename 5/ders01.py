#Gün 5, Modüller, Kütüphaneler üzerine

# hazır kütüphaneyi çalıştırmak için 3 yöntem var

#1. import komutu ile
# import math
# math kütüphanesi içerisindeki her şeyi alıyor

#2. from math import * komutu ile
#from math import cos,sin,pi yaparsak istediğimiz veya kullanmak istediğimiz komutları çekebiliyoruz.
#dir(math) komutu ile kütüphane içerisindeki komutları görebiliyoruz

#3. Default olmayan kütüphaneleri nasıl ekleriz?
#pip install flask komutu ile
#pip komutu ile internette olan paketleri yükleyebiliriz, rastgele ekleme yapamayız.

#/C/Python konumuna gidip manuel olarak library klasörüne elimizdeki kütüphaneyi atabiliriz.
"""
import math

a = math.cos(math.radians(90))
if abs(a) < 1e-10:
    a = 0.0

print(a)

print(dir(math))
print(math.factorial(6))
print(math.cos(90))
"""
import math
a = round(math.cos(math.radians(90)), 1)
print(a)

