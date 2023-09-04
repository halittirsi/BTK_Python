# Hata ayıklama
# try ---- dene
# except ----- olmazsa bunu kabul et

try:
  print(x)
except NameError:
  print("x tanımlanmamış")
except:
  print("Başka bir hata meydana geldi")

try:
    print("Merhaba")
except:
    print("Bir şeyler ters gitti")
else:
    print("Herhangi bir hata yok")

try:
  print("Merhaba")
except:
  print("Bir şeyler ters gitti")
else:
  print("Herhangi bir hata yok")

  