def o_listesi(liste):
    if len(liste) > 0:
        print(liste[0])    
        return o_listesi(liste[1:])
    
o_listesi(["ali","veli","can"])
