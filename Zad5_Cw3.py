#sposób 1

def parzystosc(x):
  if x % 2 != 0:
    return x


lista= list(filter(parzystosc,range(21)))
lista2 = []
for i in lista:
  pierwiastek = i** (1/2)
  lista2.append(pierwiastek)

print (lista2)

#sposób 2

lista3 = [i **(1/2) for i in range(21) if i % 2 != 0]

print(lista3)