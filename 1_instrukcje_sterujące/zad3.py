import random

def zgadnij_liczbe():
    iteracja=1
    x=random.randint(0,100)
    liczba_gracza=int(input("Zgadnij liczne:"))

    while x!=liczba_gracza:
        iteracja+=1
        if liczba_gracza>x:
            print("twoja liczba jest większa")
        else:
            print("twoja liczba jest mniejsza")
        liczba_gracza=int(input("Zgadnij liczbe:"))
    
    print(f'Zgadłeś liczbę {x} po {iteracja} iteracjach')
    

zgadnij_liczbe()

while True:
    grasz_dalej=input("Czy chcesz grać dalej: ")

    if grasz_dalej.lower() in ["tak","t","no pewnie"]:
        zgadnij_liczbe()
    else:
        print("Dzięki za grę !!")
        break




