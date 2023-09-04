sebze = ["domates","biber"]
meyve = ['üzüm', 'çilek', 'kivi', 'karpuz', 'incir', 'ayva', 'armut','armut']
sark = ["peynir","helva","bal"]
yesillik = ["roka","maydonoz","tere"]
pazar_listesi = [sebze, meyve, sark, yesillik,]
for dd in pazar_listesi:
    index = pazar_listesi.index(dd)
    boyut = len(dd)
    for urun in dd:
        index2 = dd.index(urun)
        print(pazar_listesi[index][index2])