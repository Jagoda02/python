#zad 3
def tworzenie_slownika(sciezka):
    with open(sciezka, 'r') as plik:
        tekst = plik.read()

    
    
    kluczG = []
    parts = tekst.split()
    slownik = {}
    zasady ='ATCG'
    yes = 1
    nie = []
    plik_nieudane = open('nieudane.txt', 'w')
    for wyraz in parts:
        if '>' in wyraz:
            kluczG.append(wyraz)
    a = 0
    try:
        for wyraz in parts:
            if wyraz.isupper():
                iloscZ = {'A':0, 'T':0, 'C':0, 'G':0}
                dlugosc = len(wyraz)
                y = 0
                while y < dlugosc:
                    if wyraz[y] != 'A' and 'T' and 'C' and 'G':
                        yes = 0
                        nie.append(kluczG[a])
                    y = y + 1
                x = 0
                
                if yes == 1:
                    while x < dlugosc:
                        if wyraz[x] == 'A':
                            iloscZ['A'] = iloscZ['A'] + 1
                        if wyraz[x] == 'T':
                            iloscZ['T'] = iloscZ['T'] + 1
                        if wyraz[x] == 'C':
                            iloscZ['C'] = iloscZ['C'] + 1
                        if wyraz[x] == 'G':
                            iloscZ['G'] = iloscZ ['G']+ 1
                        x = x + 1
                    slownik[kluczG[a]] = iloscZ
                a = a + 1
                yes = 1
    except ValueError as e:
        plik_nieudane.write(f"{nie}\n")
        
    plik_nieudane.close()
    print(slownik)
sciezka = r"C:\Users\adria\OneDrive\Dokumenty\JAGA\plik_z_fasta.fasta"
tworzenie_slownika(sciezka)
