def fac(n):
    if n <2:
        return 1
    else:
        return n * fac(n-1)
a=int(("ENTREZ UN CHIFRE "))
print( fac(a))

