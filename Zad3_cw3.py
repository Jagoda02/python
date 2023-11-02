def hamming(napis1,napis2):
  if len(napis1)!= len(napis2):
    return("Ciagi musza byc rownej dlugosci")
  else:
    licznik = 0
    dlugosc = len(napis1)
    for i in range(dlugosc):
      if napis1[i] != napis2[i]:
        licznik = licznik + 1
    return(licznik)

a = "abc"
b = "abc"

print(hamming(a,b))