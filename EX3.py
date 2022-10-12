N1 = int (input("entrez une note "))
N2 = int (input("entrez une note "))
N3 = int (input("entrez une note "))
moy=(N1+N2+N3)/3
print(moy)
if moy>=16:
    print(moy,"MENTION Très bien")
elif moy<16 and moy>= 14:
    print(moy,"MENTION Bien")
elif moy<14 and moy>= 12:
    print(moy,"MENTION  Assez Bien")
elif moy<12 and moy>= 10:
    print(moy,"MENTION  Passable")
else:
    print(moy,"Moyenne insuffisante")
