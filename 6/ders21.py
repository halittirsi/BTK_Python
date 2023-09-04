try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Dosyaya yazarken hata ile karşılaşıldı")
finally:
  f.close()