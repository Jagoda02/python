#zad 1
#CCGCGG, CCGTGG, CCACGG, CCATGG
import re
wzor = 'CC[G,A][C,T]GG'

sekwencja = 'AAACCAGGGACT'

match = re.search(wzor,sekwencja)

if match is None:
    print("Brak miejsca cięcia")
else:
    print("Występuje miejsce cięcia")
