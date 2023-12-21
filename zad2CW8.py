#zad 2
import math

def oblicz_tf(slowo, dokument):
    slowa_w_dokumencie = dokument.split()
    word_count = slowa_w_dokumencie.count(slowo)
    return word_count / len(slowa_w_dokumencie)

def oblicz_idf(slowo, korpus):
    num_documents_with_word = sum(1 for dokument in korpus if slowo in dokument)
    return 1.0 + math.log((1.0 + len(korpus)) / (1.0 + num_documents_with_word))

def oblicz_tfidf(slowo, dokument, korpus):
    tf = oblicz_tf(slowo, dokument)
    idf = oblicz_idf(slowo, korpus)
    return tf * idf

def oblicz_norme(wektor):
    return math.sqrt(sum(a**2 for a in wektor))

def oblicz_podobienstwo_cosinusowe(v1, v2):
    iloczyn_skalarny = sum(a * b for a, b in zip(v1, v2))
    norma_v1 = oblicz_norme(v1)
    norma_v2 = oblicz_norme(v2)
    
    if norma_v1 == 0 or norma_v2 == 0:
        return 0  
    
    return iloczyn_skalarny / (norma_v1 * norma_v2)

f1 = "Język programowania python jest super"
f2 = "Język programowania javascript odraża mnie"
korpus = [f1, f2]

przygotowany_korpus = [dokument.lower() for dokument in korpus]

slowa_w_f1 = set(slowo for slowo in f1.lower().split())
slowa_w_f2 = set(slowo for slowo in f2.lower().split())
unikalne_slowa = set.union(slowa_w_f1, slowa_w_f2)

reprezentacja_f1 = [oblicz_tfidf(slowo, f1, przygotowany_korpus) for slowo in unikalne_slowa]
reprezentacja_f2 = [oblicz_tfidf(slowo, f2, przygotowany_korpus) for slowo in unikalne_slowa]

podobienstwo = oblicz_podobienstwo_cosinusowe(reprezentacja_f1, reprezentacja_f2)

print(f"Podobieństwo cosinusowe między f1 a f2: {podobienstwo}")
