# time kütüphanesi 

"""
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.day)
print(x.weekday)
print(x.strftime("%B"))
print(x.)
"""
import datetime
import time
time.sleep(5)
a = input("İlk bilgiyi giriniz: ")
giris = datetime.datetime.now()
time.sleep(5)
b = input("İkinci bilgiyi giriniz: ")
cikis = datetime.datetime.now()
fark = cikis - giris
print(fark)
print(fark.seconds)
print(fark.microseconds)