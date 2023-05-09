krotka=(-10,-3,4,13,12,-6,0)

min=krotka[0]
max=krotka[0]

for i in krotka:
    if i >max:
        max=i
    elif i<min:
        min=i
    else:
        next

print('Najmniejsza liczba to:',min,'\nNajwiększa liczba to:',max)