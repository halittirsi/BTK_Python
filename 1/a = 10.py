print("Aldığınız mesafe kaç m")
alinanYol = int(input())
print("Geçiş süreniz nedir?")
gecenZaman = int(input())

ceza = alinanYol/gecenZaman > 130
print(ceza)