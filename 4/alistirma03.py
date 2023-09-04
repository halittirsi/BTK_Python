# 4 farklı listeyi tek listeye yani iç içe liste yapmış oluyoruz.
sebze = ["domates","biber"]
meyve = ['üzüm', 'çilek', 'kivi', 'karpuz', 'incir', 'ayva', 'armut','armut']
sark = ["peynir","helva","bal"]
yesillik = ["roka","maydonoz","tere"]
pazar_listesi = [sebze, meyve, sark, yesillik, "baklava"]
for i in pazar_listesi:
    if i is list:
        for urun in i:           
            print(urun)
        else:
            print(i)