lista = eval('['+ input("Informe 50 números separados por virgulas: ") +']')
numP = 0
numC = 0
for i in range(len(lista)):
    if lista[i]%2 == 0:
        numP = numP + 1
    if lista[i]%5 == 0:
        numC = numC + 1
print(numP, "de números pares")
print(numC,"de números multiplos de 5")