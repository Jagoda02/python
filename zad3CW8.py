#zad 3
import os
import sys
import datetime
import math

class TFIDF:
    def __init__(self, sciezka_do_publikacji):
        self.dane = self._wczytaj_tytuly(sciezka_do_publikacji)
        self.slowo_do_indeksu = {}
        self.idfs_ = {}
        self.slowa = set()

    def _wczytaj_tytuly(self, sciezka):
        tytuly = []
        for plik in os.listdir(sciezka):
            if plik.endswith(".pdf"):
                pelna_sciezka = os.path.join(sciezka, plik)
                tytuly.append(self._czytaj_tytul_pdf(pelna_sciezka))
        return tytuly

    def _czytaj_tytul_pdf(self, sciezka_pdf):
        return os.path.splitext(os.path.basename(sciezka_pdf))[0]

    def _buduj_slownik(self):
        for tytul in self.dane:
            slowa = tytul.split()
            for slowo in slowa:
                if slowo.isalpha():
                    self.slowa.add(slowo.lower())

    def _buduj_indeks(self):
        self.slowo_do_indeksu = {slowo: indeks for indeks, slowo in enumerate(self.slowa)}

    def _oblicz_idfs(self):
        laczna_liczba_dokumentow = len(self.dane)
        for slowo in self.slowa:
            dokumenty_z_slowem = sum(1 for tytul in self.dane if slowo.lower() in tytul.lower())
            self.idfs_[slowo] = 1.0 + math.log((1.0 + laczna_liczba_dokumentow) / (1.0 + dokumenty_z_slowem))

    def _tfidf(self, wejscie):
        liczby_słów = {slowo: wejscie.count(slowo) for slowo in self.slowa}
        tfidf_wartosci = [liczby_słów[slowo] / len(wejscie) * self.idfs_.get(slowo, 0.0) for slowo in self.slowa]
        return tfidf_wartosci

    def stworz_wektor(self):
        self._buduj_slownik()
        self._buduj_indeks()
        self._oblicz_idfs()
        wektor = []

        for tytul in self.dane:
            slowa = tytul.split()
            wektor_tytulu = self._tfidf(slowa)
            wektor.append(wektor_tytulu)

        return wektor

sciezka_do_publikacji = "ścieżka"
tfidf_instancja = TFIDF(sciezka_do_publikacji)
wektor_reprezentacji = tfidf_instancja.stworz_wektor()
print(wektor_reprezentacji)
