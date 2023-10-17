#1
#Oblicz procentową zawartość GC w poniższej sekwencji.
#Wypisz ją na ekranie z dokładnością do drugiego miejsca po przecinku.
sekwencja = 'ATGCATATGACTCAATGCCCATTAAAAA'
liczbaG = sekwencja.count('G')
liczbaC = sekwencja.count('C')
liczbaGC = (liczbaG + liczbaC)/len(sekwencja)
print(f"{liczbaGC:.2}")
