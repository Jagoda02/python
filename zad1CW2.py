def zgadywanka():
    from random import randint
    sekretna_liczba = randint(0, 20)
    tak = 0;
    ilosc = 1;
    #print(sekretna_liczba)  
 


    while tak == 0:
        liczba = input("Podaj liczbę z zakresu od 0 do 20: ")
        liczba = int(liczba)
        

       
        if liczba == sekretna_liczba:
            print(f"Gratulacje, odgadłeś liczbę, twoja liczba prób wynosi: {ilosc}")
            tak = 1
        else:
            if(liczba > sekretna_liczba):
                print("Sekretna liczba jest mniejsza")
            elif( liczba < sekretna_liczba):
                print("Sekretna liczba jest większa")
            ilosc = ilosc + 1


zgadywanka()
