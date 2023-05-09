def lista_zakupow(litera):
    lista=["burak","cukinia","pomidor","cytryna","ananas","papryka","dynia"]
    slowo=""
    result=""
    for i in lista:
        slowo=i
        if litera==slowo[0]:
            result+=slowo+" "
        else:next
    print(result)




lista_zakupow("c")
