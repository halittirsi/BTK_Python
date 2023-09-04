# defaul parametreli fonksiyonlar, kullanıcının zorunlu girmesi gerekenleri başa, zorunlu olmayanları sona yazarız, aşağıda da bahsettim.
"""
def daire(pi, r):
    alan = pi * (r**2)
    return alan
print(daire(3,5))
"""

def daire(r, pi=3.14):   # ilk önce değeri belli olanları parantez içerisine yazıyoruz, pi için 3 veya 3.14 durumu var o yüzden.
    alan = pi * (r**2)
    return alan
print(daire(5, 3.14))

# bahsettiğimiz durum aşşağıda, pi için bir değer girmedik dolayısıyla 3.14'ü kendisi atadı.

def daire(r, pi=3.14):   # ilk önce değeri belli olanları parantez içerisine yazıyoruz, pi için 3 veya 3.14 durumu var o yüzden.
    alan = pi * (r**2)
    return alan
print(daire(5))