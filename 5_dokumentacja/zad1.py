
def  wyswietl_menu():
    """Wyświetla menu"""
    print('1. Dodawanie')
    print('2. Odejmowanie')
    print('3. Mnozenie')
    print('4. Dzielenie')
    print('0. Koniec')


def wykonaj_operacje(odp):
    def dodawanie(a:float,b:float)-> float():
        """ Wykonuje dodawanie"""
        print(f'{a}+{b}={a+b}')

    def odejmowanie(a:float,b:float)-> float():
        """ Wykonuje odejmowanie"""
        print(f'{a}-{b}={a-b}')

    def mnozenie(a:float,b:float) ->float():
        print(f'{a}*{b}={a*b}')

    def dzielenie(a:float,b:float) ->float():
        """ Wykonuje dzielenie"""
        print(f'{a}/{b}={a/b}')

    """Przypisuje różne warianty operacji """
    if odp==1:
        a=int(input('Podaj liczbę a:'))
        b=int(input('Podaj liczbę b:'))
        dodawanie(a,b)
    elif odp==2:
        a=int(input('Podaj liczbę a:'))
        b=int(input('Podaj liczbę b:'))
        odejmowanie(a,b)
    elif odp==3:
        a=int(input('Podaj liczbę a:'))
        b=int(input('Podaj liczbę b:'))
        mnozenie(a,b)
    elif odp==4:
        a=int(input('Podaj liczbę a:'))
        b=int(input('Podaj liczbę b:'))
        dzielenie(a,b)
        

while True:
    """głowna pętla wykonująca program"""
    wyswietl_menu()
    odp=int(input("Wybierz operacje: "))
    if odp==0:
        break
    wykonaj_operacje(odp)





