#4
'''
Twój kolega chciałby sprawdzić czy imię jego najlepszego przyjaciela
znajduje się na liście zabawnych imion.
Najpierw chciałby ją uaktualnić o imię Harry Dixon,
ale nie potrafi programować i jego kod nie działa.
Pomóż mu naprawiając jego kod:

names_list = ("Dill Doe", "Chris P. Bacon", "Ben Dover")

names_list.append("Harry Dixon")

input = input("Podaję imię : )

b = input in names_list

print b
'''
names_list = {"Dill Doe", "Chris P. Bacon", "Ben Dover"}

names_list.add("Harry Dixon")

input = input("Podaję imię : ")

b = input in names_list

print(b)
