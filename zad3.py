#3
#Napisz program, który przyjmuje od użytkownika jego imię oraz nazwisko
#a następnie wypisuje propozycję jego adresu email w domenie student.uj.edu.pl.
#Upewnij się że zawiera tylko małe litery.

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
nazwa = f"{imie}.{nazwisko}@student.uj.edu.pl"
print(nazwa.lower())
