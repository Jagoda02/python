#zad 2

class Seq:

    def __init__(self, seq_id, seq):
        self.seq_id = seq_id
        self.seq = seq

    def __len__(self):
        return len(self.seq)

    def __str__(self):
         return self.seq

x = Seq(2, "AATTAGATG")

#dlugosc = len(x)
#sekwencja = str(x)
#print(dlugosc)
#print(sekwencja)


class RNASeq(Seq):
    zasady = "A,U,G,C"
    zasada = ""
    ile = 0
    dlugosc = 0
    wynik = 0
    GC = "G,C"
    def sekwencjaRNA(self):
        for self.zasada in self.seq:
            if self.zasada not in self.zasady:
                print(f'Bledna zasada {self.zasada}, nie ma jej w RNA!')

    def iloscGC(self):
        for self.zasada in self.seq:
            if self.zasada in self.GC:
              self.ile = self.ile + 1
        self.dlugosc = len(self.seq)
        self.wynik = (self.ile / self.dlugosc) * 100
        print(f'Zawartosc procentowa G + C to: {self.wynik}%')

class DNASeq(Seq):
    zasady = "A,T,G,C"
    zasada = ""
    def sekwencjaDNA(self):
        for self.zasada in self.seq:
            if self.zasada not in self.zasady:
                print(f'Bledna zasada {self.zasada}, nie ma jej w DNA!')

    def transcrible(self):
        sekw = self.seq
        self.seq = ""
        for self.zasada in sekw:
            if self.zasada != 'T':
                self.seq = self.seq + self.zasada
            else:
                self.seq = self.seq + 'U'
        return self.seq
    

#y = RNASeq(3, "AAGCU")
#y.sekwencjaRNA()
#y.iloscGC()
#z = DNASeq(2,"AAGTTGGCCTT")
#z.sekwencjaDNA()
#print(z.transcrible())
