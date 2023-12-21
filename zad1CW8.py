#zad 1
import math
from collections import Counter

def oblicz_tf(slowo, dokument):
    slowa_w_dokumencie = dokument.split()
    liczba_wystapien_slowa = slowa_w_dokumencie.count(slowo)
    return liczba_wystapien_slowa / len(slowa_w_dokumencie)

def oblicz_idf(slowo, korpus):
    liczba_dokumentow_z_slowa = sum(1 for dokument in korpus if slowo in dokument)
    return 1.0 + math.log((1.0 + len(korpus)) / (1.0 + liczba_dokumentow_z_slowa))

def oblicz_tfidf(slowo, dokument, korpus):
    tf = oblicz_tf(slowo, dokument)
    idf = oblicz_idf(slowo, korpus)
    return tf * idf

def przygotuj_korpus(korpus):
    return [dokument.lower() for dokument in korpus]

def main():
    f1 = "Język programowania python jest super"
    f2 = "Język programowania javascript odraża mnie"

    korpus = [f1, f2]

    przygotowany_korpus = przygotuj_korpus(korpus)

    unikalne_slowa = set(slowo for dokument in przygotowany_korpus for slowo in dokument.split())

    for slowo in unikalne_slowa:
        print(f"TF-IDF dla '{slowo}':")
        for i, dokument in enumerate(przygotowany_korpus, start=1):
            tfidf = oblicz_tfidf(slowo, dokument, przygotowany_korpus)
            print(f"  Dokument {i}: {tfidf}")

if __name__ == "__main__":
    main()
