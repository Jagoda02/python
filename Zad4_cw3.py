table_data = """
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G
"""

czesci = table_data.split()

slownik = dict(zip(czesci[::2], czesci[1::2]))


def translacja(sekwencja, slownik):
  dlugosc = len(sekwencja)
  index = 0

  while index < dlugosc:
    kodon = sekwencja[index:index +3]
    if kodon in slownik:
      aminokwasy = slownik[kodon]
    if aminokwasy == "Stop":
      raise StopIteration
    yield aminokwasy
    index = index + 3

rna_sequence = "AUGGCCAUGGCGCCCAGGUGGGCCCAAAUGGCGCCCAGGUGGGCCCAUAA"

translator = translacja(rna_sequence, slownik)

for aminokwasy in translator:
    print(aminokwasy, end=" ")