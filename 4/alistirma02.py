# 4 farklı listeyi tek listeye yani iç içe liste yapmış oluyoruz.
sebze = ["domates","biber"]
meyve = ['üzüm', 'çilek', 'kivi', 'karpuz', 'incir', 'ayva', 'armut','armut']
sark = ["peynir","helva","bal"]
yesillik = ["roka","maydonoz","tere"]
pazar_listesi = [sebze, meyve, sark, yesillik]
for i in pazar_listesi:
    print(i)            #bu satırı silebiliriz
    for urun in i:
        print(urun, end = "\t")
    print()