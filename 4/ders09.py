#tuple yöntemi
# list yöntemindeki gibi müdahaleye açık değil
# (___ , ____) parantez kullanılır ve virgül ile parantez içersinde ayırıyoruz.
# tc kimlik numaramız tuple içersinde tutulabilir ama eğitim durumumuz yada sınıfımız değişebileceği için onu tuple ile kullanmayız list yöntemi kullanılır

demet = ("Recep","Güzel")
print(demet)
print((type(demet)))

pazar = ["elma","armut","incir","karpuz","üzüm","kavun"]
pazarlik = tuple(pazar)
print(pazarlik)
print(pazarlik.index("incir"))
print(pazarlik[:2])
for meyve in pazarlik:
    print(meyve)

son_pazar = list(pazarlik)
print(son_pazar)