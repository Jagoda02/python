#zad 2
import re

dna_seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"


def translacja(kodon):
    kodony = {
         "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }
    return kodony.get(kodon, "")

def znajdowanie_ORF(dna_seq):
    kodon_start = 'ATG'
    kodon_stop = ['TAA', 'TAG', 'TGA']
    kodon_wzor = r'[ACGT]{3}'

    orf_wzor = re.compile(rf'{kodon_start}(?:{kodon_wzor})*(?:{"|".join(kodon_stop)})')

    dopasowanie = re.finditer(orf_wzor, dna_seq)
    orfy = [match.group() for match in dopasowanie]
    return orfy

def transkrypcja(seq):
    trans_seq = ""
    for zasada in seq:
        if zasada == 'T':
            trans_seq += 'A'
        elif zasada == 'G':
            trans_seq += 'C'
        elif zasada == 'A':
            trans_seq += 'U'
        elif zasada == 'C':
            trans_seq += 'G'
    return trans_seq


znalezione_orfy = znajdowanie_ORF(dna_seq)
trans = transkrypcja(dna_seq)

for orf in znalezione_orfy:
    sekwencja = ''.join([translacja(orf[i:i + 3]) for i in range(0, len(orf), 3)])
    print("ORF:", orf)
    print("Po translacji:", sekwencja)
    print()

    
