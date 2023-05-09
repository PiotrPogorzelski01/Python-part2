def palindrom(slowo):
    slowo_odwrotne=slowo[::-1]

    if slowo==slowo_odwrotne:
        print(slowo,"- jest palindromem")
    else:
        print(slowo,"- nie jest palindromem")


palindrom("kajak")