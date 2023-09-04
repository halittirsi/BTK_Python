pazar = ["elma","armut","incir","karpuz","üzüm","kavun"]

print(pazar)
print(pazar[3])
print(pazar[:2])
print(pazar[-2::])
print(pazar[3:5])

pazar.append("çilek")
print(pazar)
pazar.append("armut")
print(pazar)
print(pazar.count("armut"))     #listede kaç tane armut var onu çıktı verir
print(len(pazar))
print(pazar.index("armut"))
pazar.insert(1,"ayva")
pazar.insert(1,"kivi")
print(pazar)
pazar.pop(0)        #parametre verilmezse son elemanı siler
print(pazar)
pazar.remove("kavun")
print(pazar)
pazar.sort()
print(pazar)
pazar.reverse()
print(pazar)

dayipazar = ["domates", "biber"]        # pazar = pazar + dayipazar
pazar.extend(dayipazar)             #oluşturduğumuz diğer liste ile ilk listeyi birleştirdi
print(pazar)
pazar.clear()
print(pazar)

