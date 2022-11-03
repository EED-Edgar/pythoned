lista = eval('['+ input("Informe 20 números separados por virgula: ") +']')

par = 0

for i in range(len(lista)):
    if lista[i]%2 == 0:
        par = par + 1
print("Foram inseridos",par,"número(s) pare(s).")