lista = eval('['+ input("Informe 18 números separados por virgulas: ") +']')

for i in range(len(lista)):
    if lista[i] < 0:
        lista[i] = 0

for i in range(len(lista)):
    print(lista[i])