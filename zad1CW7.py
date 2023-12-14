#zad 1
#Napisz funkcję generującą 'losowe' sekwencje DNA o zadanej długości.
import random
zasady = ["A","T","G","C"]

dlugosc = input("Podaj dlugosc DNA: ")
dlugoscL = int(dlugosc)
dna =""
dna = random.choices(zasady, k = dlugoscL)
wynik = "".join(dna)
print(wynik)
