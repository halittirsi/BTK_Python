import time
from datetime import datetime # ya da direkt import datetime yapıp zaman = datetime.datetime.now() olmak zorunda
import math

sonDeger = 10000
sayac = 0
zaman = datetime.now()

for deger in range(2, sonDeger+1):
    kontrol = True

    for bolenSayi in range(2, int(math.sqrt(deger))+1):
        if deger % bolenSayi == 0:
            kontrol = False
            break
    if kontrol:
        sayac += 1
print()
gecenZaman = datetime.now()- zaman
print("Adet", sayac, "Geçen Zaman:", gecenZaman, "saniye")

#düzenleme olabilir kontrol et.