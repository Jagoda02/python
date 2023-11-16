#zad1
#Napisz program, który wczytuje dane z pliku data.fasta
#i przekształca je w słownik {Accession : długość sewkwencji}.

plik = open('data.fasta','r')
dane = plik.read()
plik.close()

parts = dane.split()
klucz = []
sekwencja = []
dlugosc_sekwencji = []


for wyraz in parts:
    if '>' in wyraz:
        klucz.append(wyraz)

dlugosc = len(parts)
i = 0
wielkosc = 0
tak = 0

while i < dlugosc:
    if ']' in parts[i]:
        i = i + 1
        while i < dlugosc and '>' not in parts[i]:
            if len(parts[i]) == 70:
                wielkosc = wielkosc + len(parts[i])
                tak = 1
            else:
                if tak == 0:
                    wielkosc = len(parts[i])
                    dlugosc_sekwencji.append(wielkosc)
                    wielkosc = 0
                else:
                    wielkosc = wielkosc + len(parts[i])
                    dlugosc_sekwencji.append(wielkosc)
                    wielkosc = 0
                    tak = 0
            i = i  + 1
        sekwencja = []
    i = i + 1

slownik = dict(zip(klucz,dlugosc_sekwencji))
print(slownik)
