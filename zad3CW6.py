#zad 3
import re
txt = """Would to heaven that the reader, emboldened and momentarily ferocious as he reads,
finds his wild and savage path through the desolate marshes of these dark and poisonous pages, 
without disorientation; for, unless he brings in his reading a rigorous logic and a tension of mind 
equal at least to his distrust, the mortal emanations of this book will soak his soul, as water sugar. 
It is not good for everybody to read the pages that follow; some alone will savor this bitter fruit without danger. 
Therefore, timid soul, before penetrating farther into such unexplored heaths, directs your heels back and not forward. 
Listen well to what I say to you: run your heels back and not forward, like the eyes of a son who, 
deviates respectfully from the august contemplation of the maternal side; 
or, rather, as an endless angle of chilly cranes of great meditation, which, during the winter, 
flies powerfully through the silence, with all sails stretched, towards a fixed point of the horizon, 
whence suddenly leaves a strange and strong wind, precursor of the storm. 
""".replace('\n', ' ')


#wszystkie słowa zaczynające się na literę 'm'
slowa= r'\bm\w+'
dopasowania = re.findall(slowa,txt)
#print(dopasowania)

#wszystkie wyrazy poprzedzające 'and' (włącznie z 'and')
slowa2 = r'\b\w+\s*and\b'
dopasowanie2 = re.findall(slowa2,txt)
#print(dopasowanie2)

#wszystkie wyrazy mające 7 znaków niezaczynające się na literę 'f'
slowa3 = r'\b[^f\s]\w{6}\b'
dopasowania3 = re.findall(slowa3,txt)
#print(dopasowania3)

#wszystkie słowa kończące się na 'ing' o długości <= 7
slowa4 = r'\b\w{1,7}ing\b'
dopasowanie4 = re.findall(slowa4,txt)
#print(dopasowanie4)
